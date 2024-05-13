from app.db.database import db


def get_collections():
    collections, error = db.get_collections()
    serialized_collections = []
    if error:
        return None, error
    else:
        for collection in collections:
            serialized_collections.append(collections[collection])
    return serialized_collections, error
