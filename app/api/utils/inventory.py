from app.db.database import db


def get_book_inventory(book_id):
    return db.get_book_inventory(book_id)
