from datetime import datetime
from typing import List, Optional, Literal
from uuid import UUID

from pydantic import BaseModel


class BorrowData(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    year: Optional[str]
    group: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]
    book_id: str
    due_date: datetime
    location: Literal['high', 'kinder']


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
    address: str
    phone_number: str
    gender: str


class Student(BaseModel):
    id: str
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    year: Optional[int]
    group: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]
    borrow_date: Optional[str]
    due_date: Optional[str]


class BookBorrowers(BaseModel):
    id: str
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    year: Optional[int]
    group: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]
    borrow_date: Optional[str]
    due_date: Optional[str]
    borrow_id: Optional[str]
