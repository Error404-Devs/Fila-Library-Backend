from typing import List
from fastapi import APIRouter, HTTPException, Depends
from app.api.utils.books import *
from app.api.schemas.books import *
from app.api.endpoints.auth import AuthHandler
from fastapi_pagination import Page, add_pagination, paginate
from fastapi_pagination.utils import disable_installed_extensions_check

auth_handler = AuthHandler()
books_router = APIRouter(tags=["Books"])


@books_router.get("/books", response_model=Page[BookResponse])
def books_kinder_get(title: str = None,
                     category: str = None,
                     publisher: str = None,
                     author: str = None,
                     location: str = None,
                     year: int = None,
                     admin_id: str = Depends(auth_handler.auth_wrapper)):
    admin_location, error = db.get_admin(admin_id)
    if error is None:
        if admin_location.get("role") == "high":
            response, error = get_high_books(title=title,
                                               category=category,
                                               publisher=publisher,
                                               author=author,
                                               location=location,
                                               year=year)
            if error:
                raise HTTPException(status_code=404, detail=error)
        else:
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
    else:
        raise HTTPException(status_code=404, detail=error)


add_pagination(books_router)


@books_router.post("/books", response_model=BookResponse)
def book_register(data: Book, admin_id: str = Depends(auth_handler.auth_wrapper)):
    book_data = data.model_dump()
    book_data["location"] = db.get_admin(admin_id).get("role")
    response, error = register_book(book_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response


@books_router.put("/books")  # Needs response model based on frontend needs
def book_edit(data: BookEdit, admin_id: str = Depends(auth_handler.auth_wrapper)):
    book_data = data.model_dump()
    book_data["location"] = db.get_admin(admin_id).get("role")
    response, error = edit_book(book_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response
