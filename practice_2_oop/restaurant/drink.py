from dish import Dish

class Drink(Dish):
    _volume: int

    def __init__(self, name: str, vol: int):
        self._dish_name = name
        self._volume = vol


    def get_volume(self) -> float:
        return self._volume

    def get_description(self) -> str:

        return f"Dish {self.get_name()} serves with {self.get_volume()} volume"