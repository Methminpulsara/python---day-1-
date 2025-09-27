from abc import ABC, abstractmethod
from typing import List, Dict

#   --ENCAPSULATION---------------->  ( __age) this is encapsulated in python , python have not asses modifiers

class My:
    def __init__(self , name , age):
        self.name = name
        self.__age  = age

#   --ABSTRACTION-----------------> fro it want import abstractmethod class 

class BookRepository(ABC):

    @abstractmethod
    def add_book(self, book) -> None:
        pass
