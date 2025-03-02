from abc import ABC, abstractclassmethod, abstractmethod


class Animal(ABC):
    _name: str
    _age: int
    _weight: float
    _vaccination: bool
    _feed: bool
    __id: int
    _conuter = 1

    def __init__(self, name: str, age: int, weight: float, vaccine: bool, feed: bool):
        self._name = name
        self._age = age
        self._weight = weight
        self._vaccination = vaccine
        self._feed = feed
        self.__id = self._conuter
        Animal._conuter += 1

    @abstractmethod
    def make_sound(self) -> str:
        pass

    @abstractmethod
    def move(self) -> str:
        pass

    @property
    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self._name

    def get_feed(self) -> bool:
        return self._feed


