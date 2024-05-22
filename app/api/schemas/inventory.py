from pydantic import BaseModel, model_validator
from typing import Optional
from uuid import UUID


class BookInventory(BaseModel):
    available: int
    borrowed: int


class BookInventoryRecord(BaseModel):
    book_id: Optional[UUID]
    quantity: Optional[int]
    borrow_id: Optional[UUID]

    @model_validator(mode='after')
    def check_fields(cls, values):
        book_id, quantity, borrow_id = values.book_id, values.quantity, values.borrow_id

        if borrow_id:
            if book_id or quantity:
                raise ValueError("When 'borrow_id' is provided, 'book_id' and 'quantity' must not be provided.")
        else:
            if not book_id:
                raise ValueError("'book_id' must be provided when 'borrow_id' is not present.")
            if quantity is None:
                raise ValueError("'quantity' must be provided when 'borrow_id' is not present.")

        return values
