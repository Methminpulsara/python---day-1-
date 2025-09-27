from repository import *
from dataclasses import dataclass

class LibraryExeption(Exception):
    pass
# data class use krnne nthuwa constructer widiyatat hadhla thiynne
@dataclass
class LibraryService:

    books : BookRepository
    member : MemberRepository
    loan : LoanRepository

    # def __init__(self , book : BookRepository , member : MemberRepository , loan : LoanRepository):
    #     self.book = book
    #     self.member = member
    #     self.loan = loan


    def add_book(self, book_id :str , title : str , author:str ,year : str) -> Book:
        if self.books.get_by_id(book_id) is not None:
            raise LibraryExeption("Book already exists")

        book = Book(book_id , title , author, year)

    def add_member(self , member_id:str , name :str) -> Member:
        if self.member.get_member_by_id(member_id) is not None:
            raise LibraryExeption("Member already exists")

        user = Member(member_id , name)

    def list_all_books(self):
       for book in self.books:
           print(book)
