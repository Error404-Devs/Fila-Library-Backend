from sqlalchemy.exc import SQLAlchemyError
from app.db.models.collections import Collections


def get_collections(session):
    try:
        collections = session.query(Collections).all()
        if collections:
            return Collections.serialize_collections(collections), None
        else:
            return None, "No collections found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error
