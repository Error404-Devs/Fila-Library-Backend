from pydantic import BaseModel


class Publishers(BaseModel):
    id: str
    name: str
