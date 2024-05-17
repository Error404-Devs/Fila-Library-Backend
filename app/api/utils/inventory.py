from app.db.database import db


def get_book_inventory(book_id):
    book_inventory, error = db.get_book_inventory(book_id)
    if not error:
        returned_object = {
            "available": 0,
            "borrowed": 0
        }
        for copy in book_inventory:
            if copy["status"] == "False":
                returned_object["available"] += 1
            else:
                returned_object["borrowed"] += 1
        return returned_object, None
    else:
        return None, error


