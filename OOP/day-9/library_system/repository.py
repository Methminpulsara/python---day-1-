from abc import ABC, abstractmethod
from typing import List
from models import Book


class BookRepository(ABC):

    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def get_by_id(self, book_id) -> Book:
        pass

    @abstractmethod
    def update_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass
