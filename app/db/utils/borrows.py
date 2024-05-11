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
