from sqlalchemy.exc import SQLAlchemyError
from app.db.models.email_tokens import EmailTokens


def get_email_token(session, id):
    try:
        token = session.query(EmailTokens).filter(EmailTokens.id == id).first()
        if token:
            return EmailTokens.serialize(token), None
        else:
            return None, "No token found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error


def create_email_token(session, id, user_id, expires_at, email):
    try:
        obj = EmailTokens(id=id, user_id=user_id, expires_at=expires_at, email=email)
        session.add(obj)
        return obj, None
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error


def delete_email_token(session, id):
    try:
        token = session.query(EmailTokens).filter(EmailTokens.id == id).first()
        if token:
            session.delete(token)
            return "Token deleted", None
        else:
            return None, "No token found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None, error