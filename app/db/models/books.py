import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP, ARRAY
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class KinderBooks(Base):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    title = Column(String, nullable=False)
    category = Column(String, nullable=True)
    collection_id = Column(UUID(as_uuid=True), ForeignKey("collections.id"), nullable=True)
    author_id = Column(UUID(as_uuid=True), ForeignKey("authors.id"), nullable=True)
    publisher_id = Column(UUID(as_uuid=True), ForeignKey("publishers.id"), nullable=True)
    year_of_publication = Column(Integer, nullable=True)
    place_of_publication = Column(String, nullable=True)
    ISBN = Column(String, nullable=True)
    price = Column(Integer, nullable=True)
    UDC = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)

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
            "ISBN": str(self.ISBN),
            "price": str(self.price),
            "UDC": str(self.UDC),
            "created_at": str(self.created_at)
        }

    @staticmethod
    def serialize_books(books):
        serialized_books = []
        for book in books:
            book = {
                "id": str(book.id),
                "title": str(book.title),
                "category": str(book.category),
                "collection_id": str(book.collection_id),
                "author_id": str(book.author_id),
                "publisher_id": str(book.publisher_id),
                "year_of_publication": str(book.year_of_publication),
                "place_of_publication": str(book.place_of_publication),
                "ISBN": str(book.ISBN),
                "price": str(book.price),
                "UDC": str(book.UDC),
                "created_at": str(book.created_at)
            }
            serialized_books.append(book)
        return serialized_books


class HighBooks(Base):
    __tablename__ = "books_high"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    title = Column(String, nullable=False)
    category = Column(String, nullable=True)
    collection_id = Column(UUID(as_uuid=True), ForeignKey("collections.id"), nullable=True)
    author_id = Column(UUID(as_uuid=True), ForeignKey("authors.id"), nullable=True)
    publisher_id = Column(UUID(as_uuid=True), ForeignKey("publishers.id"), nullable=True)
    year_of_publication = Column(Integer, nullable=True)
    place_of_publication = Column(String, nullable=True)
    ISBN = Column(String, nullable=True)
    price = Column(Integer, nullable=True)
    UDC = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)

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
            "ISBN": str(self.ISBN),
            "price": str(self.price),
            "UDC": str(self.UDC),
            "created_at": str(self.created_at)
        }

    @staticmethod
    def serialize_books(books):
        serialized_books = []
        for book in books:
            book = {
                "id": str(book.id),
                "title": str(book.title),
                "category": str(book.category),
                "collection_id": str(book.collection_id),
                "author_id": str(book.author_id),
                "publisher_id": str(book.publisher_id),
                "year_of_publication": str(book.year_of_publication),
                "place_of_publication": str(book.place_of_publication),
                "ISBN": str(book.ISBN),
                "price": str(book.price),
                "UDC": str(book.UDC),
                "created_at": str(book.created_at)
            }
            serialized_books.append(book)
        return serialized_books

class Wishlist(Base):
    __tablename__ = "wishlist"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("persons.id"), nullable=False, default=uuid.uuid4)
    book_id = Column(UUID(as_uuid=True), nullable=False)

    def serialize(self):
        return {
            "id": str(self.id),
            "student_id": str(self.student_id),
            "book_id": str(self.book_id)
        }

    @staticmethod
    def serialize_wishlist(books):
        serialized_books = []
        for book in books:
            book = {
                "id": str(book.id),
                "student_id": str(book.student_id),
                "book_id": str(book.book_id)
            }
            serialized_books.append(book)
        return serialized_books
