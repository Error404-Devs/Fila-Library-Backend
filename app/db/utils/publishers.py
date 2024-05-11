from sqlalchemy.exc import SQLAlchemyError
from app.db.models.publishers import Publishers


def get_publishers(session):
    try:
        publishers = session.query(Publishers).all()
        if publishers:
            return Publishers.serialize_publishers(publishers), None
        else:
            return None, "No publishers found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error
