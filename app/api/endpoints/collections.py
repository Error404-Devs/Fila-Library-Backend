from typing import List

from fastapi import APIRouter, HTTPException, Depends

from app.api.utils.collections import *
from app.api.schemas.collections import *

from app.core.security import AuthHandler

collections_router = APIRouter(tags=["Collections"])

auth_handler = AuthHandler()


@collections_router.get("/collections", response_model=List[Collections])
def collections_get(admin_id: str = Depends(auth_handler.auth_wrapper)):
    response, error = get_collections()
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response
