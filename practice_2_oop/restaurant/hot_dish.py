from dish import Dish


class HotDish(Dish):
    _temperature: float

    def __init__(self, name: str, temp: float):
        self._dish_name = name
        self._temperature = temp


    def get_temperature(self) -> float:
        return self._temperature

    def get_description(self) -> str:

        return f"Dish {self.get_name()} serves with temperature {self.get_temperature()} degree"