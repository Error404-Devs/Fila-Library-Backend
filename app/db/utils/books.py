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


def register_book(session,
                  id,
                  title,
                  category,
                  collection_id,
                  publisher_id,
                  author_id,
                  UDC,
                  year_of_publication,
                  place_of_publication,
                  ISBN,
                  price,
                  created_at):
    try:
        obj = Book(id=id,
                   title=title,
                   category=category,
                   collection_id=collection_id,
                   publisher_id=publisher_id,
                   author_id=author_id,
                   UDC=UDC,
                   year_of_publication=year_of_publication,
                   place_of_publication=place_of_publication,
                   ISBN=ISBN,
                   price=price,
                   created_at=created_at)
        session.add(obj)
        return obj
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error
