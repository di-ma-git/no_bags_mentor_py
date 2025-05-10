
class Visitor:
    __name: str
    _book_list: []
    __id: int
    _counter: int = 0


    def __init__(self, name: str):
        self.__name = name
        self._book_list = []
        self.__id = Visitor._counter
        Visitor._counter += 1

    @property
    def name(self) -> str:
        return self.__name

    def get_book_list(self) -> []:
        return self._book_list

    def take_book(self, book_name: str):
        self._book_list.append(book_name)

    def return_book(self, book_name: str):
        self._book_list.remove(book_name)

    @property
    def id(self) -> int:
        return self.__id

