from app.db.database import db


def get_publishers():
    return db.get_publishers()