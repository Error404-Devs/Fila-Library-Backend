from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel


class BorrowData(BaseModel):
    person_id: str
    book_id: str
    borrow_date: datetime
    due_date: datetime


class ReturnData(BaseModel):
    borrow_id: str


class Borrow(BaseModel):
    id: str
    person_id: str
    inventory_id: UUID
    book_id: str
    borrow_date: datetime
    due_date: datetime
    status: bool


class BorrowedItems(BaseModel):
    id: str
    book_name: str
    author_name: str
    inventory_id: str
    borrow_date: datetime
    due_date: datetime
    status: bool


class StudentBorrows(BaseModel):
    items: List[BorrowedItems]
    first_name: str
    last_name: str
    year: int
    group: str
    county: str
    city: str
    address: str
    phone_number: str
