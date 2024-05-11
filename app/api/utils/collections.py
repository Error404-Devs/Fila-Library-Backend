from app.db.database import db


def get_collections():
    return db.get_collections()
