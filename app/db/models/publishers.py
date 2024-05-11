import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class Publishers(Base):
    __tablename__ = "publishers"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    name = Column(String, nullable=False)

    def serialize(self):
        return {
            "id": str(self.id),
            "name": str(self.name)
        }

    @staticmethod
    def serialize_publishers(publishers):
        serialized_publishers = {}
        for publisher in publishers:
            serialized_publishers[str(publisher.id)] = {
                "id": str(publisher.id),
                "name": str(publisher.name)
            }
        return serialized_publishers
