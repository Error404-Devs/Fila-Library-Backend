from datetime import datetime, timedelta
import secrets
from app.db.database import db


def create_confirmation_token(person_id, email):
    format = "%Y-%m-%d %H:%M:%S"
    current_time = datetime.utcnow().strftime(format)
    expires_at = datetime.strptime(current_time, format) + timedelta(hours=12)
    id = secrets.token_urlsafe(16)

    token, error = db.create_email_token(id, person_id, expires_at, email)

    return token, error