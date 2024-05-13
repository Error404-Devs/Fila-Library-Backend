from sqlalchemy.exc import SQLAlchemyError
from app.db.models.books import Book
from app.db.models.authors import Authors


def get_books(session, title, category, publisher, author, location, year):
    try:
        books_query = session.query(Book)
        authors_query = session.query(Authors)

        # Apply filters if they exist
        if category:
            books_query = books_query.filter(Book.category == category)

        if title:
            books_query = books_query.filter(Book.title.like(f'%{title}%'))

        if publisher:
            books_query = books_query.filter(Book.publisher_id == publisher)

        if author:
            authors = authors_query.filter(
                Authors.first_name.like(f'%{author}%') | Authors.last_name.like(f'%{author}%')).all()

            if authors:
                author_ids = [author.id for author in authors]
                books_query = books_query.filter(Book.author_id.in_(author_ids))

        if location:
            books_query = books_query.filter(Book.place_of_publication == location)

        if year:
            books_query = books_query.filter(Book.year_of_publication == year)

        books = books_query.all()

        if books:
            return Book.serialize_books(books), None
        else:
            return Book.serialize_books(books), "No books found for these filters"

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
