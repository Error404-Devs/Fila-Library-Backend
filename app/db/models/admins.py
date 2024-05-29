import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class Admins(Base):
    __tablename__ = "admins"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)

    def serialize(self):
        return {
            "id": str(self.id),
            "email": str(self.email),
            "role": str(self.role),
            "hashed_password": str(self.hashed_password)
        }

    @staticmethod
    def serialize_admins(admins):
        serialized_admins = {}
        for admin in admins:
            serialized_admins[str(admin.id)] = {
                "id": str(admin.id),
                "email": str(admin.email),
                "role": str(admin.role),
                "hashed_password": str(admin.hashed_password)
        }
        return serialized_admins
