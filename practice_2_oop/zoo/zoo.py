from typing import Dict

from animal import Animal

class Zoo:
    _zoo_name: str
    __zoo_animals: Dict[int, Animal]

    def __init__(self, zoo_name: str):
        self._zoo_name = zoo_name
        self.__zoo_animals = {}


    def add_animal(self, animal: Animal):
        self.__zoo_animals[animal.get_id] = animal

    def remove_animal(self, id: int):
        del self.__zoo_animals[id]

    def show_all_animals(self):
        for i in self.__zoo_animals:
            print(f"{self.__zoo_animals.get(i).get_id}. {self.__zoo_animals.get(i).get_name()}")