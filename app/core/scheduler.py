from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app.db.database import db


def delete_expired_signup_tokens():
    print("SBLABLALB")
    email_tokens, _ = db.get_email_tokens()
    format = "%Y-%m-%d %H:%M:%S"
    current_time = datetime.utcnow()

    if email_tokens:
        for token_id in email_tokens:
            token = email_tokens[token_id]
            if datetime.strptime(token.get("expires_at"), format) < current_time:
                db.delete_email_token(token_id)


scheduler = BackgroundScheduler()

scheduler.add_job(delete_expired_signup_tokens, "interval", hours=12)