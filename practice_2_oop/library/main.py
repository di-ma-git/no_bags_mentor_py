from book import Book
from visitor import Visitor
from library import Library
from librarian import Librarian


def main():

    library = Library("Library")

    harry = Book("Harry Potter")
    azbyka = Book("Azbuka")
    happy_english = Book("Happy English")
    club = Book("Fight Club")

    tom = Visitor("Tom")
    jerry = Visitor("Jerry")

    library.add_book(harry)
    library.add_book(azbyka)
    library.add_book(happy_english)
    library.add_book(club)
    library.add_visitor(tom)
    library.add_visitor(jerry)

    library.show_all_books()
    library.show_all_visitors()


    library.take_the_book(tom, harry)
    library.take_the_book(tom, azbyka)
    library.take_the_book(jerry, happy_english)

    library.show_all_books()
    library.show_all_visitors()

    library.return_the_book(tom, harry)

    library.show_all_books()
    library.show_all_visitors()


if __name__ == "__main__":
    main()









