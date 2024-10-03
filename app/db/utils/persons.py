from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from app.db.models.persons import Person
from sqlalchemy import extract

def get_person(session, id):
    try:
        person = session.query(Person).filter(Person.id == id).first()
        if person:
            return Person.serialize(person), None
        else:
            return None, "No person found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error


def get_person_by_login_id(session, login_id):
    try:
        person = session.query(Person).filter(Person.login_id == str(login_id)).first()
        if person:
            return None, "Login id unavailable"
        else:
            return "Login id available", None
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)


def get_person_by_login_id_and_name(session, login_id, first_name):
    try:
        person = session.query(Person).filter(Person.login_id == str(login_id)).first()
        if person and person.first_name == first_name:
            return person.serialize(), None
        else:
            return None, "Could not validate credentials"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error


def get_all_login_ids(session):
    try:
        person_ids = session.query(Person.login_id).all()

        login_ids = [p[0] for p in person_ids]
        return login_ids, None
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error


def create_person(session, first_name, last_name, gender, year, group, address, phone_number, person_id, login_id, location, created_at):
    try:
        obj = Person(id=person_id,
                     login_id=login_id,
                     first_name=first_name,
                     last_name=last_name,
                     gender=gender,
                     year=year,
                     group=group,
                     address=address,
                     location=location,
                     phone_number=phone_number,
                     created_at=created_at)
        session.add(obj)
        return obj, None
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error


def edit_person(session, id, first_name, last_name, gender, year, group, address, phone_number):
    try:

        person = session.query(Person).filter(Person.id == id).first()
        person.first_name = first_name,
        person.last_name = last_name,
        person.gender = gender,
        person.year = year,
        person.group = group,
        person.address = address,
        person.phone_number = phone_number
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


def get_enrolled_persons(session, month, year, day):
    try:
        query = session.query(Person).filter(extract('month', Person.created_at) == month,
                                              extract('year', Person.created_at) == year,
                                              extract('day', Person.created_at) == day).all()
        if query:
            return Person.serialize_persons(query), None
        else:
            return [], None
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error