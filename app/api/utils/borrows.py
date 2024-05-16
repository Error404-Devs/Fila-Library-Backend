from uuid import uuid4

from app.db.database import db


def create_borrow(borrow_data):
    borrow_id = str(uuid4())
    # Update book from inventory status
    borrow_inventory, error = db.update_inventory_copy(inventory_id=borrow_data.get("inventory_id"), status=True)
    if borrow_inventory:
        borrow = db.create_borrow(borrow_id=borrow_id,
                                  person_id=borrow_data.get("person_id"),
                                  inventory_id=borrow_data.get("inventory_id"),
                                  book_id=borrow_data.get("book_id"),
                                  borrow_date=borrow_data.get("borrow_date"),
                                  due_date=borrow_data.get("due_date"),
                                  status=True)
        return borrow
    else:
        return None, error


def create_return(return_data):
    borrow_id = return_data.get("borrow_id")
    borrow_data, error = db.get_borrow_info(borrow_id)

    # Update inventory copy
    borrow_inventory, error = db.update_inventory_copy(inventory_id=borrow_data.get("inventory_id"), status=False)
    return db.return_book(borrow_id)


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
        }
        return returned_object, None
    else:
        return None, error
