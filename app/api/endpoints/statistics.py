from fastapi import APIRouter, HTTPException, Depends
statistics_router = APIRouter(tags=["Statistics"])

from app.api.utils.statistics import *
from app.api.schemas.statistics import *

from app.core.security import AuthHandler

auth_handler = AuthHandler()


@statistics_router.get("/statistics")
def monthly_statistics(month: int = None, admin_id: str = Depends(auth_handler.auth_wrapper)):
    statistics, error = get_monthly_statistics(month)
    if not error:
        return statistics
    else:
        raise HTTPException(status_code=500, detail=error)

