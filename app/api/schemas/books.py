from datetime import datetime
from typing import Optional
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


class BookResponse(BaseModel):
    id: UUID
    title: str
    category: Optional[str]
    collection_id: Optional[str]
    publisher_id: Optional[str]
    author_id: Optional[str]
    UDC: Optional[str]
    year_of_publication: Optional[str]
    place_of_publication: Optional[str]
    ISBN: Optional[str]
    price: Optional[str]
    created_at: datetime

    class Config:
        form_attributes = True