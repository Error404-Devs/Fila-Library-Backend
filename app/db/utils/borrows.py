from sqlalchemy import extract
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


def remove_inventory_item_from_borrow_record(session, borrow_id):
    try:
        borrow = session.query(Borrows).filter(Borrows.id == borrow_id).first()
        if borrow:
            borrow.inventory_id = None
            return Borrows.serialize(borrow), None
        else:
            return None, "No borrow found with this id"
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
            return Borrows.serialize_borrows(query), None
        else:
            return [], "No borrows found"
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
            return None, "No borrow found for this id"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error


def get_monthly_borrows(session, month, year):
    try:
        query = session.query(Borrows).filter(extract('month', Borrows.borrow_date) == month,
                                              extract('year', Borrows.borrow_date) == year).all()
        if query:
            return Borrows.serialize_borrows(query), None
        else:
            return None, "No borrows found for this month"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error


def get_daily_borrows(session, month, year, day):
    try:
        query = session.query(Borrows).filter(extract('month', Borrows.borrow_date) == month,
                                              extract('year', Borrows.borrow_date) == year,
                                              extract('day', Borrows.borrow_date) == day).all()
        if query:
            return Borrows.serialize_borrows(query), None
        else:
            return None, "No borrows found for this month"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error


def get_book_borrows(session, book_id):
    try:
        query = session.query(Borrows).filter(Borrows.book_id == book_id).all()
        if query:
            return Borrows.serialize_borrows(query), None
        else:
            return [], "No borrows found for this book"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error