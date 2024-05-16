from typing import List
from fastapi import APIRouter, HTTPException
from app.api.utils.borrows import *
from app.api.schemas.borrows import *

borrows_router = APIRouter(tags=["Borrows"])


@borrows_router.post("/borrows", response_model=Borrow)
def book_borrow(data: BorrowData):
    borrow_data = data.model_dump()
    response, error = create_borrow(borrow_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response


@borrows_router.post("/return", response_model=Borrow)
def book_return(data: ReturnData):
    return_data = data.model_dump()
    response, error = create_return(return_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response


@borrows_router.get("/borrows", response_model=StudentBorrows)
def student_borrows(person_id: str = None):
    borrows, error = get_student_borrows(person_id)
    if error:
        raise HTTPException(status_code=401, detail=error)
    else:
        return borrows

