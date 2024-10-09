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
        return None, error


def get_author_by_id(session, author_id):
    try:
        author = session.query(Authors).filter(Authors.id == author_id).first()
        if author:
            return Authors.serialize(author), None
        else:
            return None, "No author found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error



def create_author(session, id, first_name, last_name):
    try:
        obj = Authors(id=id,
                      first_name=first_name,
                      last_name=last_name)
        session.add(obj)
        return obj, None
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error
