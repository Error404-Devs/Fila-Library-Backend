from typing import List

from fastapi import APIRouter, HTTPException, Depends

from app.api.utils.authors import *
from app.api.schemas.authors import *

from app.core.security import AuthHandler

authors_router = APIRouter(tags=["Authors"])

auth_handler = AuthHandler()


@authors_router.get("/authors", response_model=List[Authors])
def authors_get(admin_id: str = Depends(auth_handler.auth_wrapper)):
    response, error = get_authors()
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response


@authors_router.post("/authors", response_model=Authors)
def authors_create(data: Authors, admin_id: str = Depends(auth_handler.auth_wrapper)):
    author_data = data.model_dump()
    response, error = create_authors(author_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response
