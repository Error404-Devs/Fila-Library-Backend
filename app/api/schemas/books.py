from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Book(BaseModel):
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
    copies: int


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
    quantity: Optional[int]


class BookResponse(BaseModel):
    id: UUID
    title: str
    category: Optional[str]
    collection: Optional[str]
    publisher: Optional[str]
    author: Optional[str]
    UDC: Optional[str]
    year_of_publication: Optional[str]
    place_of_publication: Optional[str]
    ISBN: Optional[str]
    price: Optional[str]
    total_copies: Optional[int]
    available_copies: Optional[int]
    borrowed_copies: Optional[int]
    created_at: datetime

    class Config:
        form_attributes = True