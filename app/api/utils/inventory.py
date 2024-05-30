from app.db.database import db
from uuid import uuid4


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


def manage_book_inventory_record(admin_id, data):
    record_data = data.model_dump()
    book_id = record_data.get("book_id")
    quantity = record_data.get("quantity")
    borrow_id = record_data.get("borrow_id")

    admin_data, _ = db.get_admin(admin_id)
    admin_role = admin_data.get("role")

    if quantity:
        # Loop through the number of copies to add or remove
        for i in range(int(abs(quantity))):
            error = None
            if quantity > 0:
                # If quantity is positive, add a new copy
                inventory_id = str(uuid4())
                db.register_copy(id=inventory_id,
                                 book_id=book_id,
                                 status=False,
                                 book_type=admin_role)
            else:
                inventory_data, error = db.get_book_inventory(book_id)
                # If quantity is negative, remove an existing copy
                for index, item in enumerate(inventory_data):
                    if not item.get("status"):
                        # Find the first available (not in use) copy
                        db.remove_copy(item.get("id"))
                        inventory_data.pop(index)
                        break

        return "Book copies added/removed successfully", error

    if borrow_id:
        # Remove inventory item from borrow record and the borrowed copy from inventory
        borrow_data, error = db.get_borrow_info(borrow_id)

        db.remove_inventory_item_from_borrow_record(borrow_id)
        db.remove_copy(borrow_data.get("inventory_id"))

        return "Book copy removed successfully", error
