from uuid import uuid4

from app.db.database import db


def get_authors():
    return db.get_authors()


def create_authors(author_data):
    author_id = str(uuid4())
    author_return = db.create_author(author_id=author_id,
                                     first_name=author_data("first_name"),
                                     last_name=author_data("last_name"))
    return author_return
