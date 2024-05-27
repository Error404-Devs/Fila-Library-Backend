from fastapi import APIRouter, HTTPException, Depends

from app.api.utils.inventory import *
from app.api.schemas.inventory import *

from app.core.security import AuthHandler

inventory_router = APIRouter(tags=["Inventory"])

auth_handler = AuthHandler()


@inventory_router.get("/inventory", response_model=BookInventory)
def books_get(book_id: str, admin_id: str = Depends(auth_handler.auth_wrapper)):
    response, error = get_book_inventory(book_id)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response


@inventory_router.post("/inventory")
def book_inventory_record_manager(record_data: BookInventoryRecord, admin_id: str = Depends(auth_handler.auth_wrapper)):
    response, error = manage_book_inventory_record(record_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response
