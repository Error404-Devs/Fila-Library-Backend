from app.db.database import db


def get_authors():
    return db.get_authors()