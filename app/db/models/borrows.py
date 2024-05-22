import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP, Boolean
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class Borrows(Base):
    __tablename__ = "borrows"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    person_id = Column(String, nullable=False)
    inventory_id = Column(UUID(as_uuid=True), ForeignKey("inventory.id"), nullable=True)
    book_id = Column(UUID(as_uuid=True), ForeignKey("books.id"), nullable=False)
    borrow_date = Column(TIMESTAMP, nullable=False)
    due_date = Column(TIMESTAMP, nullable=False)
    status = Column(Boolean, nullable=False)

    def serialize(self):
        return {
            "id": str(self.id),
            "person_id": str(self.person_id),
            "inventory_id": str(self.inventory_id),
            "book_id": str(self.book_id),
            "borrow_date": str(self.borrow_date),
            "due_date": str(self.due_date),
            "status": str(self.status)
        }

    @staticmethod
    def serialize_borrows(borrows):
        serialized_borrows = []
        for bor in borrows:
            borrow = {
                "id": str(bor.id),
                "person_id": str(bor.person_id),
                "inventory_id": str(bor.inventory_id),
                "book_id": str(bor.book_id),
                "borrow_date": str(bor.borrow_date),
                "due_date": str(bor.due_date),
                "status": str(bor.status)
            }
            serialized_borrows.append(borrow)
        return serialized_borrows
