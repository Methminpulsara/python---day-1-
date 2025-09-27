from library_service import LibraryService
from repository import *

library_service = LibraryService(books=InMemoryBookRepository , member=InMemoryMemberRepository ,loan=InMemoryLoanRepository )

while True:
    print("press 1 to list All books\n"
          "        press 2 to add Book")
def list_book():
    books: List[Book] = library_service.list_all_books()
    for book in books:
            print(f"""  ID :  {book.id}  
                        Name : {book.title}
                """)

def add_book():
    book_id = input("Enter book ID  : ")
    title = input("Enter Title : ")
    author = input("Enter Author : ")
    year: str  = input("Enter Year :")

    library_service.add_book(book_id=book_id, title=title, author=author, year=year)


