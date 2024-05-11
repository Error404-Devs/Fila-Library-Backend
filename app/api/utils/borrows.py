from uuid import uuid4

from app.db.database import db


def create_borrow(borrow_data):
    borrow_id = str(uuid4())

    borrow = db.create_borrow(borrow_id=borrow_id,
                              person_id=borrow_data.get("person_id"),
                              inventory_id=borrow_data.get("inventory_id"),
                              book_id=borrow_data.get("book_id"),
                              borrow_date=borrow_data.get("borrow_date"),
                              due_date=borrow_data.get("due_date"),
                              status=True)
    return borrow
