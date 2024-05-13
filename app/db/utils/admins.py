from sqlalchemy.exc import SQLAlchemyError
from app.db.models.admins import Admins


def get_admins(session):
    try:
        admins = session.query(Admins).all()
        if admins:
            return Admins.serialize_admins(admins), None
        else:
            return None, "No admins found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error


def get_admin(session, admin_id):
    try:
        admin = session.query(Admins).filter(Admins.id == admin_id).first()
        if admin:
            return admin.serialize(), None
        else:
            return None, "No admin found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return None, error


def create_admin(session, id, email, hashed_password):
    try:
        obj = Admins(id=id,
                     email=email,
                     hashed_password=hashed_password)
        session.add(obj)
        return obj, None
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error
