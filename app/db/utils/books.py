from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func, String

from app.db.models.books import Book
from app.db.models.authors import Authors
from app.db.models.publishers import Publishers


def get_books(session, title, category, publisher, author, location, year):
    try:
        books = None
        books_query = session.query(Book)
        authors_query = session.query(Authors)
        publishers_query = session.query(Publishers)

        # Apply filters if they exist
        if category:
            books_query = books_query.filter(func.lower(Book.category).like(f'%{category}%'))

        if title:
            books_query = books_query.filter(func.lower(Book.title).like(f'%{title.lower()}%'))

        if location and books_query:
            books_query = books_query.filter(func.lower(Book.place_of_publication).like(f'%{location}%'))

        if year and books_query:
            books_query = books_query.filter(func.cast(Book.year_of_publication, String).like(f'%{year}%'))

        if publisher:
            publishers = publishers_query.filter(
                func.lower(Publishers.name).like(f'%{publisher.lower()}%')).all()

            if publishers:
                publisher_ids = [publisher.id for publisher in publishers]
                books_query = books_query.filter(Book.publisher_id.in_(publisher_ids))
            else:
                books_query = None

        if author and books_query:
            authors = authors_query.filter(
                func.lower(Authors.first_name).like(f'%{author.lower()}%') |
                func.lower(Authors.last_name).like(f'%{author.lower()}%')
            ).all()

            if authors:
                author_ids = [author.id for author in authors]
                books_query = books_query.filter(Book.author_id.in_(author_ids))
            else:
                books_query = None


        if books_query:
            books = books_query.all()

        if books:
            return Book.serialize_books(books), None
        else:
            return None, "No books found for these filters"

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
