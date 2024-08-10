from datetime import datetime
from typing import Optional, Literal
from uuid import UUID

from pydantic import BaseModel, model_validator


class Book(BaseModel):
    title: str
    category: Optional[str]
    collection_id: Optional[UUID]
    publisher_id: Optional[UUID]
    author_id: Optional[UUID]
    UDC: Optional[str]
    year_of_publication: Optional[int]
    place_of_publication: Optional[str]
    ISBN: Optional[str]
    price: Optional[int]
    copies: int

    # inventory_numbers: Optional[list]

    # @model_validator(mode='after')
    # def check_fields(cls, values):
    #     copies, inventory_numbers = values.copies, values.inventory_numbers
    #
    #     if inventory_numbers:
    #         if len(inventory_numbers) != copies:
    #             raise ValueError("length of 'inventory_numbers' must have the same value as 'copies'")
    #
    #     return values


class BookEdit(BaseModel):
    id: UUID
    title: str
    category: Optional[str]
    collection_id: Optional[UUID]
    publisher_id: Optional[UUID]
    author_id: Optional[UUID]
    UDC: Optional[str]
    year_of_publication: Optional[int]
    place_of_publication: Optional[str]
    ISBN: Optional[str]
    price: Optional[int]


class BookResponse(BaseModel):
    id: UUID
    title: str
    category: Optional[str] = None
    collection: Optional[str] = None
    publisher: Optional[str] = None
    author: Optional[str] = None
    UDC: Optional[str] = None
    year_of_publication: Optional[str] | Optional[int] = None
    place_of_publication: Optional[str] = None
    ISBN: Optional[str] = None
    price: Optional[str] | Optional[int] = None
    total_copies: Optional[int] = None
    available_copies: Optional[int] = None
    borrowed_copies: Optional[int] = None
    created_at: datetime

    # # Returned on post only
    # added_copies: Optional[list] = None
    # existing_inventory_numbers: Optional[list] = None

    class Config:
        form_attributes = True
