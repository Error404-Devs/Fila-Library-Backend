from fastapi import APIRouter, HTTPException, Depends
statistics_router = APIRouter(tags=["Statistics"])
from starlette.responses import FileResponse

from app.api.utils.statistics import *
from app.api.schemas.statistics import *

from app.core.security import AuthHandler

auth_handler = AuthHandler()


@statistics_router.get("/statistics")
def monthly_statistics(month: int = None, year: int = None, admin_id: str = Depends(auth_handler.auth_wrapper)):
    statistics, error = get_statistics(month, year)

    if not error:
        return statistics
    else:
        raise HTTPException(status_code=500, detail=error)


@statistics_router.get("/statistics/download")
def download_monthly_statistics(month: int = None, year: int = None, admin_id: str = Depends(auth_handler.auth_wrapper)):
    statistics, error = download_statistics(month, year)

    if not error:

        return FileResponse("app/core/files/file.xlsx",
                            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                            filename=f"Statistici-{month}-{year}.xlsx")
    else:
        raise HTTPException(status_code=500, detail=error)
