from pet import Pet

class Dog(Pet):
    __type: str = "Dog"

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age, breed)


    def eat(self):
        print(f"{self.get_name()} is eating dry food")

    def walk(self):
        print(f"{self.get_name()} is walking with the owner")

    @staticmethod
    def get_type() -> str:
        return Dog.__type