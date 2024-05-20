from datetime import datetime
from uuid import uuid4

from app.db.database import db


def create_borrow(borrow_data):
    borrow_id = str(uuid4())
    person_id = borrow_data.get("person_id")
    person_info, error = db.get_person(person_id=person_id)
    if not error:
        # Update book from inventory status
        borrow_inventory, error = db.update_inventory_copy(book_id=borrow_data.get("book_id"), status=True)
        if borrow_inventory:
            borrow = db.create_borrow(borrow_id=borrow_id,
                                      person_id=borrow_data.get("person_id"),
                                      inventory_id=str(borrow_inventory),
                                      book_id=borrow_data.get("book_id"),
                                      borrow_date=datetime.utcnow(),
                                      due_date=borrow_data.get("due_date"),
                                      status=True)
            return borrow
        else:
            return None, error
    else:
        account = db.create_person(person_id=borrow_data.get("person_id"),
                                   first_name=borrow_data.get("first_name"),
                                   last_name=borrow_data.get("last_name"),
                                   gender=borrow_data.get("gender"),
                                   year=borrow_data.get("year"),
                                   group=borrow_data.get("group"),
                                   address=borrow_data.get("address"),
                                   phone_number=borrow_data.get("phone_number"))
        # Update book from inventory status
        borrow_inventory, error = db.update_inventory_copy(book_id=borrow_data.get("book_id"), status=True)
        if borrow_inventory:
            borrow = db.create_borrow(borrow_id=borrow_id,
                                      person_id=borrow_data.get("person_id"),
                                      inventory_id=borrow_inventory,
                                      book_id=borrow_data.get("book_id"),
                                      borrow_date=datetime.utcnow(),
                                      due_date=borrow_data.get("due_date"),
                                      status=True)
            return borrow
        else:
            return None, error


def create_return(return_data):
    borrow_id = return_data.get("borrow_id")
    borrow_data, error = db.get_borrow_info(borrow_id)
    if not error:
        # Update inventory copy
        borrow_inventory, _ = db.update_inventory_copy(book_id=borrow_data.get("book_id"), status=False)
        returned_object, _ = db.return_book(borrow_id)
        returned_object["inventory_id"] = borrow_inventory
        return returned_object, None
    else:
        return None, error


def get_student_borrows(person_id):
    # Verify if person is in database
    person, error = db.get_person(person_id)
    if person:
        borrows = db.get_person_borrows(person_id)
        authors_data, _ = db.get_authors()
        for borrow in borrows:
            book_info, error = db.get_book_info(borrow.get("book_id"))
            borrow["book_name"] = book_info.get("title")

            # Get author data
            author_data = authors_data[book_info.get("author_id")]
            borrow["author_name"] = author_data.get("first_name") + author_data.get("last_name")
            del borrow["book_id"], borrow["person_id"]

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


def get_book_borrows(book_id):
    return db.get_book_borrows(book_id)
