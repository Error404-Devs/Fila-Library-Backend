from pydantic import BaseModel


class Authors(BaseModel):
    id: str
    first_name: str
    last_name: str
