import re
from app.db.database import db
from uuid import uuid4
from datetime import datetime
import random

from app.api.utils.email_tokens import create_confirmation_token
from app.api.utils.borrows import get_student_borrows
from app.core.smtp import send_confirmation_email


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
        for person_id in persons_data:
            person_data = persons_data[person_id]
            books_borrowed, error = get_student_borrows(
                str(person_data.get("first_name")) + str(person_data.get("login_id"))
            )

            if not error:
                person_data["books_borrowed"] = books_borrowed["items"]

        return persons_data, None
    else:
        return None, error


def add_email_to_account(data):
    login_id = data.login_id
    email = data.email

    # Regex to separate alphabetic and numeric parts
    match = re.match(r"([a-zA-Z]+)(\d+)", login_id)

    if match:
        first_name = match.group(1)
        number = match.group(2)

    # Verify if person is in database
    person, error = db.get_person_by_login_id_and_name(number, first_name)

    if person:
        valid_email_regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

        if not re.search(valid_email_regex, email):
            return None, "Invalid email"
        else:
            response, error = create_confirmation_token(person_id=person.get("id"), email=email)

            if response:
                send_confirmation_email(receiver_email=response.email, token=response.id)

        return response, error
    else:
        return None, error


def confirm_account_email(token):
    token_data, error = db.get_email_token(token)

    if token_data:
        response, error = db.add_email_to_account(token_data.get("user_id"),
                                                  token_data.get("email"))

        if response:
            _, error = db.delete_email_token(token)

    if not error:
        return "Email confirmed", None