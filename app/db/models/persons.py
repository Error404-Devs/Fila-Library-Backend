import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class Person(Base):
    __tablename__ = "persons"

    id = Column(UUID, primary_key=True, nullable=False, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    group = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    location = Column(String, nullable=False)

    def serialize(self):
        return {
            "id": str(self.id),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "year": self.year,
            "group": self.group,
            "address": self.address,
            "phone_number": self.phone_number,
            "location": self.location
        }

    @staticmethod
    def serialize_persons(persons):
        serialized_persons = {}
        for person in persons:
            serialized_persons[str(person.id)] = {
                "id": str(person.id),
                "first_name": str(person.first_name),
                "last_name": str(person.last_name),
                "gender": str(person.gender),
                "year": str(person.year),
                "group": str(person.group),
                "address": str(person.address),
                "phone_number": str(person.phone_number),
                "location": str(person.location)
            }
        return serialized_persons
