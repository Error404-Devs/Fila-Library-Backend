from app.db.database import db


def edit_person(person_data):
    first_name = person_data.get("first_name")
    last_name = person_data.get("last_name")

    person_fetch, error = db.get_person(first_name=first_name, last_name=last_name)

    if person_fetch:
        person_data, error = db.edit_person(first_name=person_data.get("first_name"),
                                            last_name=person_data.get("last_name"),
                                            gender=person_data.get("gender"),
                                            year=person_data.get("year"),
                                            group=person_data.get("group"),
                                            address=person_data.get("address"),
                                            phone_number=person_data.get("phone_number"))
        return person_data, error
    else:
        return None, "No person found with this name"


def get_persons(first_name, last_name):
    persons_data, error = db.get_persons(first_name=first_name, last_name=last_name)
    if not error:
        return persons_data, None
    else:
        return None, error
