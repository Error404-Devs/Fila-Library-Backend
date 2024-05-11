from uuid import uuid4

from app.db.database import db


def get_publishers():
    return db.get_publishers()


def create_publisher(publisher_data):
    publisher_id = str(uuid4())
    returned_publisher = db.create_publisher(publisher_id=publisher_id,
                                             name=publisher_data.get("name"))
    return returned_publisher
