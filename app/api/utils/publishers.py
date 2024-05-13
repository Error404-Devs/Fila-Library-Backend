from uuid import uuid4

from app.db.database import db


def get_publishers():
    publishers, error = db.get_publishers()
    serialized_publishers = []
    if error:
        return None, error
    else:
        for publisher in publishers:
            serialized_publishers.append(publishers[publisher])
        return serialized_publishers, error


def create_publisher(publisher_data):
    publisher_id = str(uuid4())
    returned_publisher = db.create_publisher(publisher_id=publisher_id,
                                             name=publisher_data.get("name"))
    return returned_publisher
