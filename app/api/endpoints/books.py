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

@books_router.get("/books/student", response_model=Page[BookResponse])
def books_get(title: str = None):
    response, error = get_books_user(title=title)
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

    # Notify students about new books

    notification_response, _ = student_notify(book_data)

    return response


@books_router.put("/books") # Needs response model based on frontend needs
def book_edit(data: BookEdit, admin_id: str = Depends(auth_handler.auth_wrapper)):
    book_data = data.model_dump()
    response, error = edit_book(admin_id=admin_id, book_data=book_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response

# Book recommendation endpoint

@books_router.get("/books/recommended", response_model=List[BookRecomReturn])
def book_recommend(data: BookRecom):
    book_data = data.model_dump()
    response, error = recommend_books(book_data=book_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response

# Book wishlist endpoint

@books_router.get("/books/wishlist")
def get_wishlist(admin_id: str = Depends(auth_handler.auth_wrapper)):
    response, error = get_student_wishlist(student_id=student_id)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response

@books_router.post("/books/wishlist")
def post_wishlist(data:WishlistPost ,admin_id: str = Depends(auth_handler.auth_wrapper)):
    book_id = data.model_dump().get("book_id")
    response, error = create_student_wish(book_id=book_id, student_id=student_id)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response

@books_router.delete("/books/wishlist")
def delete_wishlist(data:WishlistPost ,admin_id: str = Depends(auth_handler.auth_wrapper)):
    book_id = data.model_dump().get("book_id")
    response, error = delete_student_wish(book_id=book_id, student_id=student_id)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response


