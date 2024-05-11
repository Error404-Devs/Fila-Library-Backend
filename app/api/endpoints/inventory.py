from fastapi import APIRouter, HTTPException

from app.api.utils.inventory import *
from app.api.schemas.inventory import *

inventory_router = APIRouter(tags=["Inventory"])


@inventory_router.get("/inventory")
def books_get(book_id: str):
    response, error = get_book_inventory(book_id)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response

