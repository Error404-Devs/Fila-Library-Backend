from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from app.db.models.persons import Person


def get_person(session, first_name, last_name):
    try:
        person = session.query(Person).filter(Person.first_name == first_name,
                                              Person.last_name == last_name).first()
        if person:
            return Person.serialize(person), None
        else:
            return None, "No person found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error


def create_person(session, first_name, last_name, gender, year, group, address, phone_number, person_id, location):
    try:
        obj = Person(id=person_id,
                     first_name=first_name,
                     last_name=last_name,
                     gender=gender,
                     year=year,
                     group=group,
                     address=address,
                     location=location,
                     phone_number=phone_number)
        session.add(obj)
        return obj, None
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error


def edit_person(session, id, first_name, last_name, gender, year, group, address, phone_number, location):
    try:

        person = session.query(Person).filter(Person.id == id).first()
        person.first_name = first_name,
        person.last_name = last_name,
        person.gender = gender,
        person.year = year,
        person.group = group,
        person.address = address,
        person.phone_number = phone_number
        person.location = location
        return person.serialize(), None
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error


def get_persons(session, first_name, last_name):
    try:
        person_query = session.query(Person)
        # Apply filters if they exist
        if first_name:
            person_query = person_query.filter(
                func.lower(func.unaccent(Person.first_name)).like(f'%{first_name.lower()}%'))

        if last_name:
            person_query = person_query.filter(
                func.lower(func.unaccent(Person.last_name)).like(f'%{last_name.lower()}%'))

        if person_query:
            return Person.serialize_persons(person_query), None
        else:
            return None, "No persons found for these filters"

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error
