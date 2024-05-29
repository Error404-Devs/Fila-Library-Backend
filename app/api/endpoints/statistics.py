from typing import List
from fastapi import APIRouter, HTTPException
statistics_router = APIRouter(tags=["Statistics"])

from app.api.utils.statistics import *
from app.api.schemas.statistics import *


@statistics_router.get("/statistics")
def monthly_statistics(month: int = None, year: int = None):
    statistics, error = get_statistics(month, year)
    if not error:
        return statistics
    else:
        raise HTTPException(status_code=404, detail=error)

