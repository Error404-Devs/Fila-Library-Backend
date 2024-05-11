from datetime import datetime
from uuid import uuid4
from app.db.database import db


def get_books(title, category, publisher, author_id, location, year):
    return db.get_books(title=title,
                        category=category,
                        publisher=publisher,
                        author_id=author_id,
                        location=location,
                        year=year)


def register_book(book_data):
    book_id = str(uuid4())
    created_at = datetime.utcnow()
    book_data["id"] = book_id
    book_data["created_at"] = created_at
    # Book register

    db.register_book(id=book_id,
                     title=book_data.get("title"),
                     category=book_data.get("category"),
                     collection_id=book_data.get("collection_id"),
                     publisher_id=book_data.get("publisher_id"),
                     author_id=book_data.get("author_id"),
                     UDC=book_data.get("UDC"),
                     year_of_publication=book_data.get("year_of_publication"),
                     place_of_publication=book_data.get("place_of_publication"),
                     ISBN=book_data.get("ISBN"),
                     price=book_data.get("price"),
                     created_at=created_at)

    # If copies are found in book_data register them in inventory

    copies = int(book_data.get("copies"))
    while copies:
        copy_id = str(uuid4())
        db.register_copy(id=copy_id,
                         book_id=book_id,
                         status=False)
        copies = copies - 1
    return book_data, None
