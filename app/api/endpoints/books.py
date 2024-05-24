from typing import List
from fastapi import APIRouter, HTTPException
from app.api.utils.books import *
from app.api.schemas.books import *

from fastapi_pagination import Page, add_pagination, paginate
from fastapi_pagination.utils import disable_installed_extensions_check

books_router = APIRouter(tags=["Books"])


@books_router.get("/books/kinder", response_model=Page[BookResponse])
def books_kinder_get(title: str = None,
                     category: str = None,
                     publisher: str = None,
                     author: str = None,
                     location: str = None,
                     year: int = None):
    response, error = get_kinder_books(title=title,
                                       category=category,
                                       publisher=publisher,
                                       author=author,
                                       location=location,
                                       year=year)
    if error:
        raise HTTPException(status_code=404, detail=error)

    disable_installed_extensions_check()
    if response:
        return paginate(response)
    else:
        return []


add_pagination(books_router)


@books_router.get("/books/high", response_model=Page[BookResponse])
def books_high_get(title: str = None,
                   category: str = None,
                   publisher: str = None,
                   author: str = None,
                   location: str = None,
                   year: int = None):
    response, error = get_high_books(title=title,
                                     category=category,
                                     publisher=publisher,
                                     author=author,
                                     location=location,
                                     year=year)
    if error:
        raise HTTPException(status_code=404, detail=error)

    disable_installed_extensions_check()
    if response:
        return paginate(response)
    else:
        return []


@books_router.post("/books", response_model=BookResponse)
def book_register(data: Book):
    book_data = data.model_dump()
    response, error = register_book(book_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response


@books_router.put("/books")  # Needs response model based on frontend needs
def book_edit(data: BookEdit):
    book_data = data.model_dump()
    response, error = edit_book(book_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response
