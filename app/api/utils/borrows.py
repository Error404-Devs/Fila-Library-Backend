from datetime import datetime
from uuid import uuid4
import re

from app.db.database import db
from app.core.smtp import book_returned_available


def create_borrow(borrow_data):
    borrow_id = str(uuid4())
    # Update book from inventory status
    borrow_inventory, error = db.update_inventory_copy(book_id=borrow_data.get("book_id"), status=True)
    if borrow_inventory:
        borrow = db.create_borrow(borrow_id=borrow_id,
                                  person_id=borrow_data.get("id"),
                                  inventory_id=str(borrow_inventory),
                                  book_id=borrow_data.get("book_id"),
                                  borrow_date=datetime.utcnow(),
                                  due_date=borrow_data.get("due_date"),
                                  status=True)
        return borrow
    else:
        return None, error

async def create_return(return_data):
    borrow_id = return_data.get("borrow_id")
    borrow_data, error = db.get_borrow_info(borrow_id)
    if not error:
        book_id = borrow_data.get("book_id")

        # Checking if book is in someone wishlist and send them a notification if exist

        wishlist, error = db.get_interested_persons(book_id=book_id)

        if wishlist:
            for wish in wishlist:
                # Fetching user and book info
                user, error = db.get_person(wish.get("student_id"))
                book, error = db.get_book_info(wish.get("book_id"), "kinder")
                if user.get("email"):
                    await book_returned_available(receiver_email=user.get("email"),
                                                  book_name=book.get("title"),
                                                  receiver_name=user.get("first_name")+user.get("last_name"))

        # Update inventory copy
        borrow_inventory, _ = db.update_inventory_copy(book_id=book_id, status=False)
        returned_object, _ = db.return_book(borrow_id)
        returned_object["inventory_id"] = borrow_inventory
        return returned_object, None
    else:
        return None, error


def get_student_borrows(login_id):

    # Regex to separate alphabetic and numeric parts
    match = re.match(r"([a-zA-Z]+)(\d+)", login_id)

    if match:
        first_name = match.group(1)
        number = match.group(2)

    # Verify if person is in database
    person, error = db.get_person_by_login_id_and_name(number, first_name)

    if person:
        person_location = person.get("location")
        borrows, error = db.get_person_borrows(id=person.get("id"))
        authors_data, _ = db.get_authors()
        if borrows:
            for borrow in borrows:
                book_info, error = db.get_book_info(borrow.get("book_id"), person_location)
                borrow["book_name"] = book_info.get("title")

                # Get author data
                if book_info["author_id"] != "None":
                    author_data = authors_data[book_info.get("author_id")]

                    borrow["author_name"] = author_data.get("first_name") + author_data.get("last_name")
                else:
                    borrow["author_name"] = ""

                borrow["id"] = borrow["book_id"]
                del borrow["person_id"]
        else:
            borrows: []

        returned_object = {
            "items": borrows,
            "first_name": person.get("first_name"),
            "last_name": person.get("last_name"),
            "address": person.get("address"),
            "year": person.get("year"),
            "group": person.get("group"),
            "county": person.get("county"),
            "city": person.get("city"),
            "phone_number": person.get("phone_number"),
            "gender": person.get("gender"),
        }
        return returned_object, None
    else:
        return None, error


def get_student_borrows_overdue(admin_id):
    returned_borrows = []
    borrows, error = db.get_all_borrows_overdue()
    # Verify if the sudents are from kinder or high

    admin, _ = db.get_admin(admin_id)

    if admin.get("role") == "kinder":
        for borrow in borrows:
            person_id = borrow.get("person_id")
            person_info, _ = db.get_person(person_id)
            if person_info.get("location") == "kinder":
                # Get book info

                book_info, _ = db.get_book_info(book_id=borrow.get("book_id"), person_location="kinder")

                del borrow["person_id"], borrow["inventory_id"], borrow["book_id"], person_info["id"]

                borrow["person_info"] = person_info
                borrow["book_name"] = book_info.get("title")
                returned_borrows.append(borrow)
    else:
        for borrow in borrows:
            person_id = borrow.get("person_id")
            person_info, _ = db.get_person(person_id)
            if person_info.get("location") == "high":

                # Get book info

                book_info, _ = db.get_book_info(book_id=borrow.get("book_id"), person_location="kinder")

                del borrow["person_id"], borrow["inventory_id"], borrow["book_id"], person_info["id"]

                borrow["person_info"] = person_info
                borrow["book_name"] = book_info.get("title")
                returned_borrows.append(borrow)
    return returned_borrows, None


def get_book_borrowers(book_id):
    book_borrows, error = db.get_book_borrows(book_id)
    if book_borrows:
        persons = []
        for item in book_borrows:
            if item.get("status") == "True":
                person_data, _ = db.get_person(item.get("person_id"))
                if person_data:
                    person_data["borrow_date"] = item.get("borrow_date")
                    person_data["due_date"] = item.get("due_date")
                    person_data["borrow_id"] = item.get("id")
                    persons.append(person_data)
        return persons, None
    return None, error
