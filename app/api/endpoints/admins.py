from fastapi import APIRouter, HTTPException, Response, Depends, Cookie

from app.api.utils.admins import *
from app.api.schemas.admins import *

from app.core.security import AuthHandler

admins_router = APIRouter(tags=["Admins"])

auth_handler = AuthHandler()


@admins_router.post("/admins/login", response_model=LoginResponse)
def admin_login(admin_data: AdminLogin, response: Response):
    login_response, error = login(admin_data)
    if error:
        raise HTTPException(status_code=409, detail=error)
    else:
        access_token, refresh_token = auth_handler.generate_tokens(login_response.get("id"))
        login_response["access_token"] = access_token
        response.set_cookie(key="refresh_token",
                            value=refresh_token,
                            secure=True,
                            httponly=True,
                            domain=".onrender.com",
                            path="/api",
                            samesite="none")
    return login_response


@admins_router.get("/admins/logout")
def admin_logout(response: Response):
    response.set_cookie(key="refresh_token",
                        value="",
                        secure=True,
                        httponly=True,
                        domain=".onrender.com",
                        path="/api",
                        samesite="none")
    return {"detail": "Logged out"}


@admins_router.get("/admins/refresh_token", response_model=LoginResponse)
def refresh_token(refresh_token: str | None = Cookie(None)):
    refresh_response, error = token_refresh(refresh_token)
    if error:
        raise HTTPException(status_code=401, detail=error)
    return refresh_response


# endpoint for testing
@admins_router.get("/admins/protected")
def protected(user_id: str = Depends(auth_handler.auth_wrapper)):
    return {"user_id": user_id}
