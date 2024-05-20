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


def create_person(session, first_name, last_name, gender, year, group, address, phone_number, person_id):
    try:
        obj = Person(id=person_id,
                     first_name=first_name,
                     last_name=last_name,
                     gender=gender,
                     year=year,
                     group=group,
                     address=address,
                     phone_number=phone_number)
        session.add(obj)
        return obj
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error