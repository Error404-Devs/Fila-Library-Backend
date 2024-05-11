from pydantic import BaseModel


class Publishers(BaseModel):
    id: str
    name: str


class PublisherCreate(BaseModel):
    name: str
