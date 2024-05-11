from datetime import datetime

from pydantic import BaseModel


class BorrowData(BaseModel):
    person_id: str
    inventory_id: str
    book_id: str
    borrow_date: datetime
    due_date: datetime


class Borrow(BaseModel):
    id: str
    person_id: str
    inventory_id: str
    book_id: str
    borrow_date: datetime
    due_date: datetime
    status: bool

