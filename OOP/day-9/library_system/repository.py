# repository.py
from abc import ABC, abstractmethod
from typing import List, Dict
from models import Book, Member, Loan

class BookRepository(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None: pass

    @abstractmethod
    def get_by_id(self, book_id) -> Book: pass

    @abstractmethod
    def update_book(self, book: Book) -> None: pass

    @abstractmethod
    def get_all_books(self) -> List[Book]: pass


class MemberRepository(ABC):
    @abstractmethod
    def add_member(self, member: Member) -> None: pass

    @abstractmethod
    def get_member_by_id(self, member_id) -> Member: pass

    @abstractmethod
    def get_member_list(self) -> List[Member]: pass


class LoanRepository(ABC):
    @abstractmethod
    def add_loan(self, loan: Loan) -> None: pass

    @abstractmethod
    def get_by_id(self, loan_id) -> Loan: pass

    @abstractmethod
    def update_loan(self, loan: Loan) -> None: pass

    @abstractmethod
    def get_all_loans(self) -> List[Loan]: pass


# In-memory implementations
class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.__books: Dict[str, Book] = {}

    def get_by_id(self, book_id) -> Book:
        return self.__books.get(book_id)

    def update_book(self, book: Book) -> None:
        self.__books[book.book_id] = book

    def get_all_books(self) -> List[Book]:
        return list(self.__books.values())

    def add_book(self, book: Book) -> None:
        self.__books[book.book_id] = book


class InMemoryMemberRepository(MemberRepository):
    def __init__(self):
        self.members: Dict[str, Member] = {}

    def add_member(self, member: Member) -> None:
        self.members[member.member_id] = member

    def get_member_by_id(self, member_id) -> Member:
        return self.members.get(member_id)

    def get_member_list(self) -> List[Member]:
        return list(self.members.values())


class InMemoryLoanRepository(LoanRepository):
    def __init__(self):
        self.loans: Dict[str, Loan] = {}

    def add_loan(self, loan: Loan) -> None:
        self.loans[loan.loan_id] = loan

    def get_by_id(self, loan_id) -> Loan:
        return self.loans.get(loan_id)

    def update_loan(self, loan: Loan) -> None:
        self.loans[loan.loan_id] = loan

    def get_all_loans(self) -> List[Loan]:
        return list(self.loans.values())
