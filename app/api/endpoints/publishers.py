from fastapi import APIRouter, HTTPException

from app.api.utils.publishers import *
from app.api.schemas.publishers import *

publishers_router = APIRouter(tags=["Publishers"])


@publishers_router.get("/publishers", response_model=Publishers)
def publishers_get():
    response, error = get_publishers()
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response
