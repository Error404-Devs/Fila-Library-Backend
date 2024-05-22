from sqlalchemy.exc import SQLAlchemyError
from app.db.models.inventory import Inventory


def get_book_inventory(session, book_id):
    try:
        copies = session.query(Inventory).filter(Inventory.book_id == book_id).all()
        if copies:
            return Inventory.serialize_copies(copies), None
        else:
            return [], "No copies found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error


def get_books_inventory(session):
    try:
        copies = session.query(Inventory).all()
        if copies:
            return Inventory.serialize_copies(copies), None
        else:
            return None, "No copies found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error


def register_copy(session, id, book_id, status):
    try:
        obj = Inventory(id=id,
                        book_id=book_id,
                        status=status)
        session.add(obj)
        return obj
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error


def remove_copy(session, inventory_id):
    try:
        copy = session.query(Inventory).filter(Inventory.id == inventory_id).first()
        if copy:
            session.delete(copy)
            return copy
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error


def update_inventory_copy(session, book_id, status):
    try:
        copy = session.query(Inventory).filter(Inventory.book_id == book_id).first()
        if copy:
            copy.status = status
            session.commit()
            return copy.id, None
        else:
            return None, "Copy from inventory not found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error