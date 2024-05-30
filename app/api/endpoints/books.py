from fastapi import APIRouter, HTTPException, Depends
from app.api.utils.books import *
from app.api.schemas.books import *

from app.core.security import AuthHandler

from fastapi_pagination import Page, add_pagination, paginate
from fastapi_pagination.utils import disable_installed_extensions_check

books_router = APIRouter(tags=["Books"])

auth_handler = AuthHandler()


@books_router.get("/books", response_model=Page[BookResponse])
def books_get(admin_id: str = Depends(auth_handler.auth_wrapper),
              title: str = None,
              category: str = None,
              publisher: str = None,
              author: str = None,
              location: str = None,
              year: int = None):
    response, error = get_books(admin_id=admin_id,
                                title=title,
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


@books_router.post("/books", response_model=BookResponse)
def book_register(data: Book, admin_id: str = Depends(auth_handler.auth_wrapper)):
    book_data = data.model_dump()
    response, error = register_book(admin_id=admin_id, book_data=book_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response


@books_router.put("/books") # Needs response model based on frontend needs
def book_edit(data: BookEdit, admin_id: str = Depends(auth_handler.auth_wrapper)):
    book_data = data.model_dump()
    response, error = edit_book(admin_id=admin_id, book_data=book_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response
