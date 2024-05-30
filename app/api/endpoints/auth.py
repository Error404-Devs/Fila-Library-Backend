from fastapi import APIRouter, HTTPException

from app.api.utils.auth import *
from app.api.schemas.auth import *
from app.core.config import ACCESS_EXPIRY

from app.core.security import AuthHandler

auth_router = APIRouter(tags=["Authentication"])

auth_handler = AuthHandler()


@auth_router.post("/auth/login", response_model=LoginResponse)
def admin_login(admin_data: AdminLogin):
    login_response, error = login(admin_data)
    if error:
        raise HTTPException(status_code=409, detail=error)
    else:
        access_token, refresh_token = auth_handler.generate_tokens(login_response.get("id"))
        login_response["access_token"] = access_token
        login_response["refresh_token"] = refresh_token
        login_response["expires_in"] = ACCESS_EXPIRY
    return login_response


@auth_router.get("/auth/refresh_token", response_model=RefreshResponse)
def refresh_token(refresh_token: str):
    refresh_response, error = token_refresh(refresh_token)
    if error:
        raise HTTPException(status_code=401, detail=error)
    refresh_response["expires_in"] = ACCESS_EXPIRY
    return refresh_response
