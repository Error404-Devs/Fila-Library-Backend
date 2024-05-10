import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class Authors(Base):
    __tablename__ = "authors"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    def serialize(self):
        return {
            "id": str(self.id),
            "first_name": str(self.title),
            "last_name": str(self.category)
        }

    @staticmethod
    def serialize_authors(authors):
        serialized_authors = {}
        for author in authors:
            serialized_authors[str(author.id)] = {
                "id": str(author.id),
                "first_name": str(author.title),
                "last_name": str(author.category)
        }
        return serialized_authors
