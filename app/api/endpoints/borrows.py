from fastapi import APIRouter, HTTPException, Depends
from app.api.utils.borrows import *
from app.api.schemas.borrows import *

from app.core.security import AuthHandler

borrows_router = APIRouter(tags=["Borrows"])

auth_handler = AuthHandler()


@borrows_router.post("/borrows", response_model=Borrow)
def book_borrow(data: BorrowData):
    borrow_data = data.model_dump()
    response, error = create_borrow(borrow_data=borrow_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response


@borrows_router.post("/return", response_model=Borrow)
def book_return(data: ReturnData, admin_id: str = Depends(auth_handler.auth_wrapper)):
    return_data = data.model_dump()
    response, error = create_return(return_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response


@borrows_router.get("/borrows/book", response_model=List[BookBorrowers])
def book_borrowers(book_id: str = None, admin_id: str = Depends(auth_handler.auth_wrapper)):
    response, error = get_book_borrowers(book_id=book_id)
    if error:
        raise HTTPException(status_code=404, detail=error)
    return response


@borrows_router.get("/borrows", response_model=Optional[StudentBorrows])
def student_borrows(first_name: str = None,
                    last_name: str = None):
    borrows, error = get_student_borrows(first_name=first_name, last_name=last_name)
    if error:
        raise HTTPException(status_code=401, detail=error)
    elif borrows["items"] or borrows["items"] == []:
        return borrows
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@borrows_router.get("/borrows/overdue", response_model=List[OverDue])
def student_borrows_overdue(admin_id: str = Depends(auth_handler.auth_wrapper)):
    borrows, error = get_student_borrows_overdue(admin_id)
    if error:
        raise HTTPException(status_code=401, detail=error)
    elif borrows:
        return borrows
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")

