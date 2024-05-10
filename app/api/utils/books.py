from app.db.database import db


def get_books():
    return db.get_books()
