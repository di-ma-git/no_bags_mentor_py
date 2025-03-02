
class Book:
    __name: str
    __author: str
    __description: str
    __id: int
    _counter: int = 0
    _is_accessible: bool

    def __init__(self, name: str, author: str = None, description: str = None):
        self.__name = name
        self.__author = author
        self.__description = description
        self._is_accessible = True
        self.__id = Book._counter
        Book._counter += 1

    @property
    def name(self) -> str:
        return self.__name

    @property
    def author(self) -> str:
        return self.__author

    @property
    def description(self) -> str:
        return self.__description


    @property
    def id(self) -> int:
        return self.__id

    def get_is_accessible(self) -> bool:
        if self._is_accessible:
            print(f"{self.__name} is accessible, you can take it for reading")
        else:
            print(f"{self.__name} isn't accessible, you can't take it for reading")
        return self._is_accessible

    def set_is_accessible(self, is_accessible: bool):
        self._is_accessible = is_accessible
        print(f"{self.__name} is accessible: {self._is_accessible}")
