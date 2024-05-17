from pydantic import BaseModel


class BookInventory(BaseModel):
    available: int
    borrowed: int
