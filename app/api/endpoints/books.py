from typing import List

from fastapi import APIRouter, HTTPException

from app.api.utils.books import *
from app.api.schemas.books import *

books_router = APIRouter(tags=["Books"])


@books_router.get("/books", response_model=List[BookResponse])
def books_get():
    response, error = get_books()
    print(response)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response


@books_router.post("/books", response_model=BookResponse)
def book_register(data: Book):
    book_data = data.model_dump()
    response, error = register_book(book_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response
