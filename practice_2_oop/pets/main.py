from dog import Dog
from cat import Cat
from pet_app import PetApp

def main():
    sharik = Dog("Sharik", 5, "dvorterier")
    barsik = Cat("Barsik", 6, "prosto kot")
    murzik = Cat("Murzik", 3, "tai")

    app = PetApp("Pet store")
    app.add_pet(sharik)
    app.add_pet(barsik)
    app.add_pet(murzik)

    app.show_all_pets()

    sharik.walk()
    sharik.eat()
    barsik.play()
    murzik.eat()


if __name__ == "__main__":
    main()