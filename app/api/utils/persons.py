from app.db.database import db
from uuid import uuid4
from datetime import datetime
import random


def create_person(person_data, admin_id):
    person_id = str(uuid4())

    def generate_unique_login_id():
        # Needs fix later, whenever all ids are used it creates an infinite loop
        while True:
            login_id = random.randint(1000, 9999)

            _, error = db.get_person_by_login_id(login_id)
            if not error:
                return login_id

    login_id = generate_unique_login_id()
    created_at = datetime.utcnow()
    admin_location, error = db.get_admin(admin_id)

    if not error:
        person_data, error = db.create_person(person_id=person_id,
                                              login_id=login_id,
                                              first_name=person_data.get("first_name"),
                                              last_name=person_data.get("last_name"),
                                              gender=person_data.get("gender"),
                                              year=person_data.get("year"),
                                              group=person_data.get("group"),
                                              address=person_data.get("address"),
                                              phone_number=person_data.get("phone_number"),
                                              location=admin_location.get("role"),
                                              created_at=created_at)
        return person_data, error
    else:
        return None, error


def edit_person(person_data):
    person_data, error = db.edit_person(id=person_data.get("id"),
                                        first_name=person_data.get("first_name"),
                                        last_name=person_data.get("last_name"),
                                        gender=person_data.get("gender"),
                                        year=person_data.get("year"),
                                        group=person_data.get("group"),
                                        address=person_data.get("address"),
                                        phone_number=person_data.get("phone_number"))
    return person_data, error


def get_persons(first_name, last_name):
    persons_data, error = db.get_persons(first_name=first_name, last_name=last_name)
    if not error:
        return persons_data, None
    else:
        return None, error
