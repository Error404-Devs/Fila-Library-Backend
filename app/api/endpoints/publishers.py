from typing import List

from fastapi import APIRouter, HTTPException, Depends

from app.api.utils.publishers import *
from app.api.schemas.publishers import *

from app.core.security import AuthHandler

publishers_router = APIRouter(tags=["Publishers"])

auth_handler = AuthHandler()


@publishers_router.get("/publishers", response_model=List[Publishers])
def publishers_get(admin_id: str = Depends(auth_handler.auth_wrapper)):
    response, error = get_publishers()
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response


@publishers_router.post("/publishers", response_model=Publishers)
def publisher_create(data: PublisherCreate, admin_id: str = Depends(auth_handler.auth_wrapper)):
    publisher_data = data.model_dump()
    response, error = create_publisher(publisher_data)
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response
