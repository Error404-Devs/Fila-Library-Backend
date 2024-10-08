from fastapi import APIRouter, HTTPException, Depends

from app.api.utils.persons import *
from app.api.schemas.persons import *

from app.core.security import AuthHandler

persons_router = APIRouter(tags=["Persons"])

auth_handler = AuthHandler()


@persons_router.post("/persons", response_model=NewStudent)
def person_create(data: StudentCreate, admin_id: str = Depends(auth_handler.auth_wrapper)):
    person_data = data.model_dump()
    response, error = create_person(person_data=person_data, admin_id=admin_id)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response


@persons_router.put("/persons")
def person_update(data: StudentUpdate, admin_id: str = Depends(auth_handler.auth_wrapper)):
    person_data = data.model_dump()
    response, error = edit_person(person_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return {"message": "Update successful"}


@persons_router.get("/persons")
def persons_fetch(first_name: str = None,
                  last_name: str = None):
    response, error = get_persons(first_name=first_name, last_name=last_name)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response


@persons_router.put("/persons/email")
def add_email(data: EmailRequest):
    response, error = add_email_to_account(data)
    if error:
        raise HTTPException(status_code=406, detail=error)
    return response


@persons_router.post("/persons/email")
def confirm_email(token: str):
    response, error = confirm_account_email(token)
    if error:
        raise HTTPException(status_code=406, detail=error)
    return response