from sqlalchemy.exc import SQLAlchemyError
from app.db.models.borrows import Borrows


def create_borrow(session,
                  borrow_id,
                  person_id,
                  inventory_id,
                  book_id,
                  borrow_date,
                  due_date,
                  status):
    try:
        obj = Borrows(id=borrow_id,
                      person_id=person_id,
                      inventory_id=inventory_id,
                      book_id=book_id,
                      borrow_date=borrow_date,
                      due_date=due_date,
                      status=status)
        session.add(obj)
        return obj, None
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error


def return_book(session, borrow_id):
    try:
        borrow = session.query(Borrows).filter(Borrows.id == borrow_id).first()
        if borrow:
            borrow.status = False
            session.commit()
            return Borrows.serialize(borrow), None
        else:
            return None, "No borrow found with this id"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error


def get_person_borrows(session, person_id):
    try:
        query = session.query(Borrows).filter(Borrows.person_id == person_id).all()
        if query:
            return Borrows.serialize_borrows(query)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error


def get_borrow_info(session, borrow_id):
    try:
        query = session.query(Borrows).filter(Borrows.id == borrow_id).first()
        if query:
            return Borrows.serialize(query), None
        else:
            return None, "No borrow found for this person"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error