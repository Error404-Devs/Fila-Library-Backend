from sqlalchemy.exc import SQLAlchemyError
from app.db.models.books import Book


def get_books(session, title, category, publisher, author_id, location, year):
    try:
        query = session.query(Book)
        # Apply filters if they exist
        if category:
            query = query.filter(Book.categories.any(category))
        if title:
            query = query.filter(Book.title == title)
        if publisher:
            query = query.filter(Book.publisher_id == publisher)
        if author_id:
            query = query.filter(Book.author_id == author_id)
        if location:
            query = query.filter(Book.place_of_publication == location)
        if year:
            query = query.filter(Book.year_of_publication == year)

        books = query.all()

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
