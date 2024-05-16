from pydantic import BaseModel


class AdminLogin(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    email: str
    access_token: str
    refresh_token: str
    expires_in: int


class RefreshResponse(BaseModel):
    email: str
    access_token: str
    expires_in: int