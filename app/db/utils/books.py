from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func, String

from app.db.models.books import Book
from app.db.models.authors import Authors
from app.db.models.publishers import Publishers
from sqlalchemy import func, String
from sqlalchemy.exc import SQLAlchemyError


def get_books(session, title=None, category=None, publisher=None, author=None, location=None, year=None):
    try:
        books_query = session.query(Book)
        authors_query = session.query(Authors)
        publishers_query = session.query(Publishers)

        # Apply filters if they exist
        if category:
            books_query = books_query.filter(
                func.lower(func.unaccent(Book.category)).like(f'%{category.lower()}%'))

        if title:
            books_query = books_query.filter(
                func.lower(func.unaccent(Book.title)).like(f'%{title.lower()}%'))

        if location:
            books_query = books_query.filter(
                func.lower(func.unaccent(Book.place_of_publication)).like(f'%{location.lower()}%'))

        if year:
            books_query = books_query.filter(
                func.cast(Book.year_of_publication, String).like(f'%{year}%'))

        if publisher:
            publishers = publishers_query.filter(
                func.lower(func.unaccent(Publishers.name)).like(f'%{publisher.lower()}%')
            ).all()

            if publishers:
                publisher_ids = [publisher.id for publisher in publishers]
                books_query = books_query.filter(Book.publisher_id.in_(publisher_ids))
            else:
                return None, "No books found for these filters"

        if author:
            authors = authors_query.filter(
                func.lower(func.unaccent(Authors.first_name)).like(f'%{author.lower()}%') |
                func.lower(func.unaccent(Authors.last_name)).like(f'%{author.lower()}%')
            ).all()

            if authors:
                author_ids = [author.id for author in authors]
                books_query = books_query.filter(Book.author_id.in_(author_ids))
            else:
                return None, "No books found for these filters"

        books = books_query.all()

        if books:
            return Book.serialize_books(books), None
        else:
            return None, "No books found for these filters"

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error


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


def edit_book(session,
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
              price):
    try:
        book = session.query(Book).filter(Book.id == id).first()
        if book:
            book.title = title
            book.category = category
            book.collection_id = collection_id
            book.publisher_id = publisher_id
            book.author_id = author_id
            book.UDC = UDC
            book.year_of_publication = year_of_publication
            book.place_of_publication = place_of_publication
            book.ISBN = ISBN
            book.price = price
            return book.serialize(), None
        else:
            return None, "Book not found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error


def get_book_info(session, book_id):
    try:
        book = session.query(Book).filter(Book.id == book_id).first()
        if book:
            return Book.serialize(book), None
        else:
            return None, "No books found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error