from uuid import uuid4

from app.db.database import db


def create_borrow(borrow_data):
    borrow_id = str(uuid4())
    # Update book from inventory status
    borrow_inventory, error = db.update_inventory_copy(inventory_id=borrow_data.get("inventory_id"))
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


def get_student_borrows(student_id):
    borrows, error = db.get_person_borrows(student_id)
    authors_data, _ = db.get_authors()
    for borrow in borrows:
        book_info, error = db.get_book_info(borrow.get("book_id"))
        borrow["book_name"] = book_info.get("title")

        # Get author data
        author_data = authors_data[book_info.get("author_id")]
        borrow["author_name"] = author_data.get("first_name") + author_data.get("last_name")
        del borrow["book_id"], borrow["person_id"]
    return borrows, error
