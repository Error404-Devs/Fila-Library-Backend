from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func, String

from app.db.models.books import KinderBooks, HighBooks, Wishlist
from app.db.models.authors import Authors
from app.db.models.publishers import Publishers
from sqlalchemy import func, String
from sqlalchemy.exc import SQLAlchemyError


def get_kinder_books(session, title=None, category=None, publisher=None, author=None, location=None, year=None):
    try:
        books_query = session.query(KinderBooks)
        authors_query = session.query(Authors)
        publishers_query = session.query(Publishers)

        # Apply filters if they exist
        if category:
            books_query = books_query.filter(
                func.lower(func.unaccent(KinderBooks.category)).like(f'%{category.lower()}%'))

        if title:
            books_query = books_query.filter(
                func.lower(func.unaccent(KinderBooks.title)).like(f'%{title.lower()}%'))

        if location:
            books_query = books_query.filter(
                func.lower(func.unaccent(KinderBooks.place_of_publication)).like(f'%{location.lower()}%'))

        if year:
            books_query = books_query.filter(
                func.cast(KinderBooks.year_of_publication, String).like(f'%{year}%'))

        if publisher:
            publishers = publishers_query.filter(
                func.lower(func.unaccent(Publishers.name)).like(f'%{publisher.lower()}%')
            ).all()

            if publishers:
                publisher_ids = [publisher.id for publisher in publishers]
                books_query = books_query.filter(KinderBooks.publisher_id.in_(publisher_ids))
            else:
                return None, "No books found for these filters"

        if author:
            authors = authors_query.filter(
                func.lower(func.unaccent(Authors.first_name)).like(f'%{author.lower()}%') |
                func.lower(func.unaccent(Authors.last_name)).like(f'%{author.lower()}%')
            ).all()

            if authors:
                author_ids = [author.id for author in authors]
                books_query = books_query.filter(KinderBooks.author_id.in_(author_ids))
            else:
                return None, "No books found for these filters"

        books = books_query.all()

        if books:
            return KinderBooks.serialize_books(books), None
        else:
            return None, "No books found for these filters"

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error


def get_high_books(session, title=None, category=None, publisher=None, author=None, location=None, year=None):
    try:
        books_query = session.query(HighBooks)
        authors_query = session.query(Authors)
        publishers_query = session.query(Publishers)

        # Apply filters if they exist
        if category:
            books_query = books_query.filter(
                func.lower(func.unaccent(HighBooks.category)).like(f'%{category.lower()}%'))

        if title:
            books_query = books_query.filter(
                func.lower(func.unaccent(HighBooks.title)).like(f'%{title.lower()}%'))

        if location:
            books_query = books_query.filter(
                func.lower(func.unaccent(HighBooks.place_of_publication)).like(f'%{location.lower()}%'))

        if year:
            books_query = books_query.filter(
                func.cast(HighBooks.year_of_publication, String).like(f'%{year}%'))

        if publisher:
            publishers = publishers_query.filter(
                func.lower(func.unaccent(Publishers.name)).like(f'%{publisher.lower()}%')
            ).all()

            if publishers:
                publisher_ids = [publisher.id for publisher in publishers]
                books_query = books_query.filter(HighBooks.publisher_id.in_(publisher_ids))
            else:
                return None, "No books found for these filters"

        if author:
            authors = authors_query.filter(
                func.lower(func.unaccent(Authors.first_name)).like(f'%{author.lower()}%') |
                func.lower(func.unaccent(Authors.last_name)).like(f'%{author.lower()}%')
            ).all()

            if authors:
                author_ids = [author.id for author in authors]
                books_query = books_query.filter(HighBooks.author_id.in_(author_ids))
            else:
                return None, "No books found for these filters"

        books = books_query.all()

        if books:
            return HighBooks.serialize_books(books), None
        else:
            return None, "No books found for these filters"

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error


def register_kinder_book(session,
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
        obj = KinderBooks(id=id,
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
        return None, error


def register_high_book(session,
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
        obj = HighBooks(id=id,
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
        return None, error


def edit_kinder_book(session,
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
        book = session.query(KinderBooks).filter(KinderBooks.id == id).first()
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


def edit_high_book(session,
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
        book = session.query(HighBooks).filter(HighBooks.id == id).first()
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


def get_book_info(session, book_id, person_location):
    try:
        if person_location == "kinder":
            book = session.query(KinderBooks).filter(KinderBooks.id == book_id).first()
            if book:
                return KinderBooks.serialize(book), None
            else:
                return None, "No books found"
        else:
            book = session.query(HighBooks).filter(HighBooks.id == book_id).first()
            if book:
                return HighBooks.serialize(book), None
            else:
                return None, "No books found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error

# Wishlist functions

def get_student_wishlist(session, student_id):
    try:
        query = session.query(Wishlist).filter(Wishlist.student_id == student_id).all()
        if query:
            return Wishlist.serialize_wishlist(query), None
        else:
            return None, "User does not have any books in wishlist."
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error

def create_student_wish(session, student_id, wish_id, book_id):
    try:
        obj = Wishlist(id=wish_id,
                        student_id=student_id,
                        book_id=book_id)

        session.add(obj)
        return obj.serialize(), None
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error

def delete_student_wish(session, wish_id):
    try:
        query = session.query(Wishlist).filter(Wishlist.id == wish_id).first()
        if query:
            session.delete(query)
            return query.serialize(), None
        else:
            return None, "Copy from inventory not found"


    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error

