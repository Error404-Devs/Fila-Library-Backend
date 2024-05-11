from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager

from app.core.config import USER, PASSWORD, HOST, DB_PORT, DB_NAME

Base = declarative_base()

from app.db.utils.books import *
from app.db.utils.authors import *
from app.db.utils.collections import *
from app.db.utils.publishers import *
from app.db.utils.inventory import *
from app.db.utils.borrows import *

engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{DB_PORT}/{DB_NAME}')

Base.metadata.create_all(bind=engine)


@contextmanager
def session_scope():
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class DataBase:

    # BOOKS

    @staticmethod
    def get_books(title, category, publisher, author_id, location, year):
        with session_scope() as session:
            return get_books(session=session,
                             title=title,
                             category=category,
                             publisher=publisher,
                             author_id=author_id,
                             location=location,
                             year=year)

    @staticmethod
    def register_book(id, title, category, collection_id, publisher_id, author_id,
                      UDC, year_of_publication, place_of_publication, ISBN, price, created_at):
        with session_scope() as session:
            return register_book(session=session,
                                 id=id,
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

    # AUTHORS

    @staticmethod
    def get_authors():
        with session_scope() as session:
            return get_authors(session)

    @staticmethod
    def create_author(author_id, first_name, last_name):
        with session_scope() as session:
            return create_author(session=session,
                                 id=author_id,
                                 first_name=first_name,
                                 last_name=last_name)

    # COLLECTIONS

    @staticmethod
    def get_collections():
        with session_scope() as session:
            return get_collections(session)

    # PUBLISHERS

    @staticmethod
    def get_publishers():
        with session_scope() as session:
            return get_publishers(session)

    @staticmethod
    def create_publisher(publisher_id, name):
        with session_scope() as session:
            return create_publisher(session=session,
                                    publisher_id=publisher_id,
                                    name=name)

    # INVENTORY

    @staticmethod
    def register_copy(id, book_id, status):
        with session_scope() as session:
            return register_copy(session=session,
                                 id=id,
                                 book_id=book_id,
                                 status=status)

    @staticmethod
    def get_book_inventory(book_id):
        with session_scope() as session:
            return get_book_inventory(session=session, book_id=book_id)

    # BORROWS

    @staticmethod
    def create_borrow(borrow_id, person_id, inventory_id, book_id, borrow_date, due_date, status):
        with session_scope() as session:
            return create_borrow(session=session,
                                 borrow_id=borrow_id,
                                 person_id=person_id,
                                 inventory_id=inventory_id,
                                 book_id=book_id,
                                 borrow_date=borrow_date,
                                 due_date=due_date,
                                 status=status)


db = DataBase()
