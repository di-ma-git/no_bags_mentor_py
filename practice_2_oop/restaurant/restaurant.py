from typing import Dict
from dish import Dish

class Restaurant:
    __restaurant_name: str
    _menu: Dict[str, Dish]

    def __init__(self, name: str):
        self.__restaurant_name = name
        self._menu = {}

    @property
    def restaurant_name(self) -> str:
        return self.__restaurant_name

    def add_dish(self, dish: Dish):
        self._menu[dish.get_name()] = dish

    def remove_dish(self):
        # TODO document why this method is empty
        pass

    def show_menu(self):
        for value in self._menu.values():
            print(f"{value.get_name()} - {value.get_description()}")
