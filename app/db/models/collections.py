import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class Collections(Base):
    __tablename__ = "collections"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    name = Column(String, nullable=False)

    def serialize(self):
        return {
            "id": str(self.id),
            "name": str(self.name)
        }

    @staticmethod
    def serialize_collections(collections):
        serialized_collections = {}
        for collection in collections:
            serialized_collections[str(collection.id)] = {
                "id": str(collection.id),
                "name": str(collection.name)
            }
        return serialized_collections
