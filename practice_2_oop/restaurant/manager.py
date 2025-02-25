from restaurant import Restaurant
from dish import Dish


class Manager:
    __manager_name: str

    def __init__(self, name: str):
        self.__manager_name = name
        self._restaurant = None

    @property
    def manager_name(self) -> str:
        return self.__manager_name

    def set_restaurant(self, rest: Restaurant):
        self._restaurant = rest

    def manage(self, restaurant: Restaurant, dish: Dish):
        restaurant.add_dish(dish)
        restaurant.show_menu()
