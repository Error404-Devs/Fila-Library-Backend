from fastapi import APIRouter, HTTPException

from app.api.utils.authors import *
from app.api.schemas.authors import *

authors_router = APIRouter(tags=["Authors"])


@authors_router.get("/authors", response_model=Authors)
def authors_get():
    response, error = get_authors()
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response
