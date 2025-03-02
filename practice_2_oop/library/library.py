from typing import Dict
from visitor import  Visitor
from book import  Book

class Library:
    _name: str
    _books: {}
    _visitors: Dict[int, Visitor]

    def __init__(self, name: str):
        self._name = name
        self._books = {}
        self._visitors = {}

    def add_book(self, book: Book):
        if book.id not in self._books.keys():
            self._books[book.id] = book
        else:
            print(f"Book with {book.id} is already in the library")

    def add_visitor(self, visitor: Visitor):
        if visitor.id not in self._visitors.keys():
            self._visitors[visitor.id] = visitor
        else:
            print(f"Book with {visitor.id} is already in the library")

    def take_the_book(self, visitor: Visitor, book: Book):
        visitor.take_book(book.name)
        book.set_is_accessible(False)

    def return_the_book(self, visitor: Visitor, book: Book):
        visitor.return_book(book.name)
        book.set_is_accessible(True)

    def show_all_books(self):
        for value in self._books.values():
            print(f"{value.id}. {value.name}, is accessible: {value.get_is_accessible()}")

    def show_all_visitors(self):
        for value in self._visitors.values():
            print(f"{value.id}. {value.name}: {value.get_book_list()}")
