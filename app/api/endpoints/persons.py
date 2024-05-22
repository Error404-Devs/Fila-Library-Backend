from fastapi import APIRouter, HTTPException

from app.api.utils.persons import *
from app.api.schemas.persons import *

persons_router = APIRouter(tags=["Persons"])


@persons_router.put("/persons")
def person_update(data: Student):
    person_data = data.model_dump()
    response, error = edit_person(person_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return {"message": "Update successful"}
