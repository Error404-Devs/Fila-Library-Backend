from typing import Optional

from pydantic import BaseModel


class Student(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    year: Optional[int]
    group: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]
