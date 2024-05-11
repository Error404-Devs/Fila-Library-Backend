from fastapi import APIRouter, HTTPException

from app.api.utils.collections import *
from app.api.schemas.collections import *

collections_router = APIRouter(tags=["Collections"])


@collections_router.get("/collections", response_model=Collections)
def collections_get():
    response, error = get_collections()
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response
