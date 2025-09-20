from abc import ABC, abstractmethod
from typing import List

from models import *


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


class MemberRepository(ABC):

    @abstractmethod
    def add_member(self, member: Member) -> None:
        pass

    @abstractmethod
    def get_member_by_id(self, member_id) -> Member:
        pass

    @abstractmethod
    def get_member_list(self) -> List[Member]:
        pass


class LoanRepository(ABC):

    @abstractmethod
    def add_loan(self, loan: Loan) -> None:
        pass

    @abstractmethod
    def get_by_id(self, loan_id) -> Loan:
        pass

    @abstractmethod
    def update_loan(self, book: Loan) -> None:
        pass

    @abstractmethod
    def get_all_loans(self) -> List[Loan]:
        pass


class InMemoryBookRepository(BookRepository):
    def get_by_id(self, book_id) -> Book:
        pass

    def update_book(self, book: Book) -> None:
        pass

    def get_all_books(self) -> List[Book]:
        pass

    def add_book(self, book: Book) -> None:
        pass