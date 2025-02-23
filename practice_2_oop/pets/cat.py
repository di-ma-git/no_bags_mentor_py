from pet import Pet

class Cat(Pet):
    __type: str = "Cat"

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age, breed)


    def eat(self):
        print(f"{self.get_name()} is eating wet food")

    def play(self):
        print(f"{self.get_name()} is playing with the owner")

    @staticmethod
    def get_type() -> str:
        return Cat.__type