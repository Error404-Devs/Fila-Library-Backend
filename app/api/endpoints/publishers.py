from typing import List

from fastapi import APIRouter, HTTPException

from app.api.utils.publishers import *
from app.api.schemas.publishers import *

publishers_router = APIRouter(tags=["Publishers"])


@publishers_router.get("/publishers", response_model=List[Publishers])
def publishers_get():
    response, error = get_publishers()
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response


@publishers_router.post("/publishers", response_model=Publishers)
def publisher_create(data: PublisherCreate):
    publisher_data = data.model_dump()
    response, error = create_publisher(publisher_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response
