from animal import Animal
from feedable import Feedable


class Mammal(Animal, Feedable):
    _type_of_mammal: str
    _number_of_legs: int
    _sound: str

    def __init__(self, name: str, age: int,
                 weight: float, type_of_mammal: str = None, sound: str = None,
                 vaccine: bool = False, feed: bool = False, number_of_legs: int = 2):
        super().__init__(name, age, weight, vaccine, feed)
        self._number_of_legs = number_of_legs
        self._type_of_mammal = type_of_mammal
        self._sound = sound

    def move(self) -> None:
        print(f"{self._name} can run or walk")

    def make_sound(self) -> None:
        print(f"{self._name} makes {self._sound}")

    def get_type(self) -> str:
        return self._type_of_mammal

    def to_feed(self):
        if not self._feed:
            self._feed = True
            print(f"You've just fed {self._name}")
        else:
            print(f"{self._name} is already well-fed")