from fastapi import APIRouter, HTTPException

from app.api.utils.books import *


books_router = APIRouter(tags=["Books"])


@books_router.get("/books")
def books_get():
    response, error = get_books()
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response
