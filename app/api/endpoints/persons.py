from fastapi import APIRouter, HTTPException, Depends

from app.api.utils.persons import *
from app.api.schemas.persons import *

from app.core.security import AuthHandler

persons_router = APIRouter(tags=["Persons"])

auth_handler = AuthHandler()


@persons_router.put("/persons")
def person_update(data: Student, admin_id: str = Depends(auth_handler.auth_wrapper)):
    person_data = data.model_dump()
    response, error = edit_person(person_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return {"message": "Update successful"}
