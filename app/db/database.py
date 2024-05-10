from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager

from app.core.config import USER, PASSWORD, HOST, DB_PORT, DB_NAME

Base = declarative_base()

from app.db.utils.books import *
from app.db.utils.authors import *

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
    def get_books():
        with session_scope() as session:
            return get_books(session)

    # AUTHORS

    @staticmethod
    def get_authors():
        with session_scope() as session:
            return get_authors(session)

db = DataBase()
