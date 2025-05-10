from manager import Manager
from hot_dish import HotDish
from drink import Drink
from restaurant import Restaurant


def main():

    restik = Restaurant("Restik")

    manager_max = Manager("Max")

    borsh = HotDish("Borsh", 60)
    kvas = Drink("Kvas", 500)

    manager_max.manage(restik, borsh)
    manager_max.manage(restik, kvas)




if __name__ == "__main__":
    main()