from datetime import datetime
from uuid import uuid4
from app.db.database import db


def get_books(admin_id, title, category, publisher, author, location, year):
    publishers_data, _ = db.get_publishers()
    collections_data, _ = db.get_collections()
    authors_data, _ = db.get_authors()
    inventory_data, _ = db.get_books_inventory()

    admin_data, _ = db.get_admin(admin_id)
    admin_role = admin_data.get("role")

    if admin_role == "kinder":
        books_data, error = db.get_kinder_books(title=title,
                                                category=category,
                                                publisher=publisher,
                                                author=author,
                                                location=location,
                                                year=year)
    else:
        books_data, error = db.get_high_books(title=title,
                                              category=category,
                                              publisher=publisher,
                                              author=author,
                                              location=location,
                                              year=year)

    if error:
        return None, error
    sorted_books_data = sorted(books_data, key=lambda x: x["title"])
    for book in sorted_books_data:
        publisher_name, collection_name, author_name = None, None, None

        publisher = publishers_data.get(book["publisher_id"])
        if publisher:
            publisher_name = publisher.get("name")

        collection = collections_data.get(book["collection_id"])
        if collection:
            collection_name = collection.get("name")

        author = authors_data.get(book["author_id"])
        if author:
            author_first_name = authors_data.get(book["author_id"]).get("first_name")
            author_last_name = authors_data.get(book["author_id"]).get("last_name")
            author_name = " ".join(filter(None, [author_first_name, author_last_name]))

        borrowed_count = 0
        available_count = 0
        for item in inventory_data:
            if item.get("book_id") == book.get("id"):
                if item.get("status"):
                    borrowed_count += 1
                else:
                    available_count += 1

        book["borrowed_copies"] = borrowed_count
        book["available_copies"] = available_count
        book["total_copies"] = borrowed_count + available_count
        book["publisher"] = publisher_name
        book["collection"] = collection_name
        book["author"] = author_name
    return sorted_books_data, None

def get_books_user(title):
    books_data, error = db.get_kinder_books(title=title,
                                            category=None,
                                            publisher=None,
                                            author=None,
                                            location=None,
                                            year=None)
    sorted_books_data = sorted(books_data, key=lambda x: x["title"])
    return sorted_books_data, None



def register_book(admin_id, book_data):
    book_id = str(uuid4())
    created_at = datetime.utcnow()
    book_data["id"] = book_id
    book_data["created_at"] = created_at

    admin_data, _ = db.get_admin(admin_id)
    admin_role = admin_data.get("role")
    # Book register
    if admin_role == "kinder":
        db.register_kinder_book(id=book_id,
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
    else:
        db.register_high_book(id=book_id,
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
    book_data["total_copies"] = copies
    book_data["available_copies"] = copies

    added_copies = []
    existing_inventory_numbers = []
    while copies:
        inventory_numbers = book_data.get("inventory_numbers")

        copy, _ = db.get_book_inventory_by_inventory_number(inventory_numbers[-1])

        if copy:
            existing_inventory_numbers.append(inventory_numbers[-1])
            book_data["existing_inventory_numbers"] = existing_inventory_numbers
        else:
            inventory_id = str(uuid4())
            copy = db.register_copy(id=inventory_id,
                                    book_id=book_id,
                                    status=False,
                                    book_type=admin_role,
                                    inventory_number=inventory_numbers[-1])

            added_copies.append(copy.get("number"))
            book_data["added_copies"] = added_copies

        copies = copies - 1
        inventory_numbers.pop()
    return book_data, None


def edit_book(admin_id, book_data):
    book_location = book_data.get("location")

    admin_data, _ = db.get_admin(admin_id)
    admin_role = admin_data.get("role")

    if admin_role == "kinder":
        book_data, error = db.edit_kinder_book(id=book_data.get("id"),
                                               title=book_data.get("title"),
                                               category=book_data.get("category"),
                                               collection_id=book_data.get("collection_id"),
                                               publisher_id=book_data.get("publisher_id"),
                                               author_id=book_data.get("author_id"),
                                               UDC=book_data.get("UDC"),
                                               year_of_publication=book_data.get("year_of_publication"),
                                               place_of_publication=book_data.get("place_of_publication"),
                                               ISBN=book_data.get("ISBN"),
                                               price=book_data.get("price"))
    else:
        book_data, error = db.edit_high_book(id=book_data.get("id"),
                                             title=book_data.get("title"),
                                             category=book_data.get("category"),
                                             collection_id=book_data.get("collection_id"),
                                             publisher_id=book_data.get("publisher_id"),
                                             author_id=book_data.get("author_id"),
                                             UDC=book_data.get("UDC"),
                                             year_of_publication=book_data.get("year_of_publication"),
                                             place_of_publication=book_data.get("place_of_publication"),
                                             ISBN=book_data.get("ISBN"),
                                             price=book_data.get("price"))

    return book_data, error
