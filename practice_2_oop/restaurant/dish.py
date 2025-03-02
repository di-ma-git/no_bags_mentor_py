from abc import ABC, abstractmethod

class Dish(ABC):
    _dish_name: str

    @abstractmethod
    def get_description(self) -> str:
        pass

    def get_name(self) -> str:
        return self._dish_name