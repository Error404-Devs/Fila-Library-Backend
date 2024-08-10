import uuid
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base

from app.db.models.books import KinderBooks, HighBooks


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    book_id = Column(UUID(as_uuid=True), nullable=False)
    # number = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False)
    book_type = Column(String, nullable=False)

    # Define a custom validator function
    def validate_book_id(self, session):
        if self.book_type == "kinder":
            book_exists = session.query(KinderBooks).filter_by(id=self.book_id).first()
        elif self.book_type == "high":
            book_exists = session.query(HighBooks).filter_by(id=self.book_id).first()
        else:
            return False

        return book_exists is not None

    def serialize(self):
        return {
            "id": str(self.id),
            "book_id": str(self.book_id),
            # "number": int(self.number),
            "book_type": str(self.book_type),
            "status": self.status
        }

    @staticmethod
    def serialize_copies(copies):
        serialized_copies = []
        for copy in copies:
            serialized_copy = {
                "id": str(copy.id),
                "book_id": str(copy.book_id),
                # "number": int(copy.number),
                "book_type": str(copy.book_type),
                "status": copy.status
            }
            serialized_copies.append(serialized_copy)
        return serialized_copies
