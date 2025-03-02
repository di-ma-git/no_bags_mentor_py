
from mammal import Mammal
from bird import Bird
from zoo import Zoo


def main():
    zoo1 = Zoo("First Zoo")
    elephant_petya = Mammal("Elephant Petya", 10, 200, "Elephant", "tu-tu-ru")
    chicken_zoya = Bird("Chicken Zoya", 1, 3, False, "Ko-ko-ko")

    elephant_petya.to_feed()
    chicken_zoya.to_feed()
    print(elephant_petya.get_feed())
    print(chicken_zoya.get_feed())
    elephant_petya.move()
    elephant_petya.make_sound()
    chicken_zoya.move()
    chicken_zoya.make_sound()

    zoo1.add_animal(elephant_petya)
    zoo1.add_animal(chicken_zoya)
    zoo1.show_all_animals()





if __name__ == "__main__":
    main()


