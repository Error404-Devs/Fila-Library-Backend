from datetime import datetime
from typing import Optional, Literal
from uuid import UUID

from pydantic import BaseModel


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
    location: Literal["high", "kinder"]


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
    location: Literal["high", "kinder"]


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

    class Config:
        form_attributes = True
