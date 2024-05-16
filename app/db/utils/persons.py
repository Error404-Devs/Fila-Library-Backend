from sqlalchemy.exc import SQLAlchemyError
from app.db.models.persons import Person


def get_person(session, person_id):
    try:
        person = session.query(Person).filter(Person.id == person_id).first()
        if person:
            return Person.serialize(person), None
        else:
            return None, "No person found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error