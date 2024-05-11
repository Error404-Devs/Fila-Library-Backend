from sqlalchemy.exc import SQLAlchemyError
from app.db.models.authors import Authors


def get_authors(session):
    try:
        authors = session.query(Authors).all()
        if authors:
            return Authors.serialize_authors(authors), None
        else:
            return None, "No authors found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error
