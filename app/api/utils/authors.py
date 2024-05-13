from uuid import uuid4

from app.db.database import db


def get_authors():
    authors, error = db.get_authors()
    serialized_authors = []
    for author in authors:
        serialized_authors.append(authors[author])
    return serialized_authors, error


def create_authors(author_data):
    author_id = str(uuid4())
    author_return = db.create_author(author_id=author_id,
                                     first_name=author_data("first_name"),
                                     last_name=author_data("last_name"))
    return author_return
