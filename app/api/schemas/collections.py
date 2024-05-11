from pydantic import BaseModel


class Collections(BaseModel):
    id: str
    name: str
