import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class EmailTokens(Base):
    __tablename__ = "email_tokens"

    id = Column(String, primary_key=True, nullable=False, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("persons.id"), nullable=False)
    expires_at = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "expires_at": self.expires_at,
            "email": self.email
        }

    @staticmethod
    def serialize_email_tokens(email_tokens):
        serialized_email_tokens = {}
        for token in email_tokens:
            serialized_email_tokens[str(token.id)] = {
                "id": token.id,
                "user_id": token.user_id,
                "expires_at": token.expires_at,
                "email": token.email,
            }
        return serialized_email_tokens
