import uuid
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    collection_id = Column(UUID(as_uuid=True), ForeignKey("collections.id"), nullable=False)
    author_id = Column(UUID(as_uuid=True), ForeignKey("authors.id"), nullable=False)
    publisher_id = Column(UUID(as_uuid=True), ForeignKey("publishers.id"), nullable=False)
    year_of_publication = Column(Integer, nullable=False)
    place_of_publication = Column(String, nullable=False)
    copies_count = Column(Integer, nullable=False)
    ISBN = Column(String, nullable=True)
    UDC = Column(String, nullable=True)

    def serialize(self):
        return {
            "id": str(self.id),
            "title": str(self.title),
            "category": str(self.category),
            "collection_id": str(self.collection_id),
            "author_id": str(self.author_id),
            "publisher_id": str(self.publisher_id),
            "year_of_publication": str(self.year_of_publication),
            "place_of_publication": str(self.place_of_publication),
            "copies_count": self.copies_count,
            "ISBN": str(self.ISBN),
            "UDC": str(self.UDC)
        }

    @staticmethod
    def serialize_books(books):
        serialized_books = {}
        for book in books:
            serialized_books[str(book.id)] = {
                "id": str(book.id),
                "title": str(book.title),
                "category": str(book.category),
                "collection_id": str(book.collection_id),
                "author_id": str(book.author_id),
                "publisher_id": str(book.publisher_id),
                "year_of_publication": str(book.year_of_publication),
                "place_of_publication": str(book.place_of_publication),
                "copies_count": book.copies_count,
                "ISBN": str(book.ISBN),
                "UDC": str(book.UDC)
        }
        return serialized_books
