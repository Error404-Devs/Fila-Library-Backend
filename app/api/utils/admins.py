from uuid import uuid4

from app.db.database import db
from app.core.security import AuthHandler

auth_handler = AuthHandler()


def login(admin_data):
    login_data = admin_data.model_dump()
    admins_data, _ = db.get_admins()

    for key in admins_data:
        if admins_data[key].get("email") == login_data.get("email"):
            user_data = admins_data[key]

            if auth_handler.verify_password(login_data.get("password"), user_data.get("hashed_password")):
                login_data["email"] = user_data.get("email")
                login_data["id"] = user_data.get("id")

                return login_data, False
            else:
                return login_data, "Incorrect password"
    return login_data, "Incorrect email"


def token_refresh(refresh_token):
    access_token, admin_id = auth_handler.refresh_token(refresh_token)
    admin_data, error = db.get_admin(admin_id)
    admin_data["access_token"] = access_token

    if error:
        return None, "Could not validate credentials"

    return admin_data, None