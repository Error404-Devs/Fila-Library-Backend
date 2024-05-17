from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager

from app.core.config import USER, PASSWORD, HOST, DB_PORT, DB_NAME

Base = declarative_base()

from app.db.utils.books import *
from app.db.utils.admins import *
from app.db.utils.authors import *
from app.db.utils.collections import *
from app.db.utils.publishers import *
from app.db.utils.inventory import *
from app.db.utils.borrows import *
from app.db.utils.persons import *

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
    def get_books(title, category, publisher, author, location, year):
        with session_scope() as session:
            return get_books(session=session,
                             title=title,
                             category=category,
                             publisher=publisher,
                             author=author,
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

    @staticmethod
    def get_book_info(book_id):
        with session_scope() as session:
            return get_book_info(session=session, book_id=book_id)

    # ADMINS

    @staticmethod
    def get_admins():
        with session_scope() as session:
            return get_admins(session)

    @staticmethod
    def get_admin(admin_id):
        with session_scope() as session:
            return get_admin(session, admin_id)

    @staticmethod
    def create_admin(admin_id, email, hashed_password):
        with session_scope() as session:
            return create_admin(session=session,
                                id=admin_id,
                                email=email,
                                hashed_password=hashed_password)

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

    @staticmethod
    def update_inventory_copy(book_id, status):
        with session_scope() as session:
            return update_inventory_copy(session=session, book_id=book_id, status=status)

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

    @staticmethod
    def return_book(borrow_id):
        with session_scope() as session:
            return return_book(session=session,
                               borrow_id=borrow_id)

    @staticmethod
    def get_person_borrows(person_id):
        with session_scope() as session:
            return get_person_borrows(session=session, person_id=person_id)

    @staticmethod
    def get_borrow_info(borrow_id):
        with session_scope() as session:
            return get_borrow_info(session=session, borrow_id=borrow_id)

    # PERSONS

    @staticmethod
    def get_person(person_id):
        with session_scope() as session:
            return get_person(session=session, person_id=person_id)

    # STATISTICS

    @staticmethod
    def get_monthly_borrows(month):
        with session_scope() as session:
            return get_monthly_borrows(session=session, month=month)

db = DataBase()
