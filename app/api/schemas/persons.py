from typing import Optional

from pydantic import BaseModel


class StudentUpdate(BaseModel):
    id: str
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    year: Optional[int]
    group: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]
    location: Optional[str]

class StudentCreate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    year: Optional[int]
    group: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]