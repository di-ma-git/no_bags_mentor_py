from abc import ABC, abstractmethod
import uuid

class Pet(ABC):
    _pet_name: str
    _pet_age: int
    __breed: str
    __pet_id: str

    def __init__(self, name: str, age: int, breed: str):
        self._pet_name = name
        self._pet_age = age
        self.__breed = breed
        self.__pet_id = str(uuid.uuid4())

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @property
    def pet_id(self) -> str:
        return self.__pet_id

    def get_name(self) -> str:
        return self._pet_name

    def get_age(self) -> int:
        return self._pet_age

    def get_breed(self) -> str:
        return self.__breed

    def set_name(self, name: str):
        self._pet_name = name

    def set_age(self, age: int):
        self._pet_age = age