import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class Person(Base):
    __tablename__ = "persons"

    id = Column(UUID, primary_key=True, nullable=False, default=uuid.uuid4)
    login_id = Column(Integer, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    gender = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    group = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    location = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

    def serialize(self):
        return {
            "id": str(self.id),
            "login_id": self.login_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "year": self.year,
            "group": self.group,
            "address": self.address,
            "phone_number": self.phone_number,
            "location": self.location,
            "email": self.email,
            "created_at": self.created_at
        }

    @staticmethod
    def serialize_persons(persons):
        serialized_persons = {}
        for person in persons:
            serialized_persons[str(person.id)] = {
                "id": str(person.id),
                "login_id": str(person.login_id),
                "first_name": str(person.first_name),
                "last_name": str(person.last_name),
                "gender": str(person.gender),
                "year": str(person.year),
                "group": str(person.group),
                "address": str(person.address),
                "phone_number": str(person.phone_number),
                "location": str(person.location),
                "email": str(person.email),
                "created_at": str(person.created_at)
            }
        return serialized_persons
