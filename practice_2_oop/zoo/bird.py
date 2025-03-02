from animal import Animal
from feedable import Feedable


class Bird(Animal, Feedable):
    _sound: str
    _like_water: bool

    def __init__(self, name: str, age: int,
                 weight: float, like_water: bool = False, sound: str = None,
                 vaccine: bool = False, feed: bool = False):
        super().__init__(name, age, weight, vaccine, feed)
        self._like_water = like_water
        self._sound = sound

    def move(self) -> None:
        if self._like_water:
            print(f"{self._name} can fly and swim")
        else:
            print(f"{self._name} can fly")


    def make_sound(self) -> None:
        print(f"{self._name} makes {self._sound}")

    def get_type(self) -> bool:
        return self._like_water

    def to_feed(self):
        if not self._feed:
            self._feed = True
            print(f"You've just fed {self._name}")
        else:
            print(f"{self._name} is already well-fed")