from sqlalchemy.exc import SQLAlchemyError
from app.db.models.books import Book


def get_books(session):
    try:
        books = session.query(Book).all()
        if books:
            return Book.serialize_books(books), None
        else:
            return None, "No books found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error
