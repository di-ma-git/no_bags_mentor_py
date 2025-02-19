from conditions import get_number
from enum import Enum





def main():
    # Реализуйте программу, которая принимает с консоли день недели (число от 1 до 7)
    # и выводит название дня (например, 1 — "Понедельник")
    print(get_day_of_week(int(get_number())))

    # Принимает с консоли название планеты (значение из перечисления).
    # Выводит порядковый номер планеты от Солнца и примерное значение её массы относительно Земли.
    try:
        user_input = input("Please input name of planet: ").strip().upper()

        planet = Planet[user_input]

        print(f"Порядковый номер: {planet.order}, Масса: {planet.mass}")

    except KeyError:
        print("Ошибка: Такой планеты нет в солнечной системе!")

    except Exception as e:
        print(f"Ошибка: {str(e)}")

    # Напишите калькулятор с использованием switch
    result1 = calc(5, 5, "*")
    print(result1)
    result2 = calc(5, 5, "/")
    print(result2)
    result3 = calc(5, 5, "-")
    print(result3)



class Planet(Enum):
    MERCURY = (1, 3.301e23)
    VENUS = (2, 4.867e24)
    EARTH = (3, 5.972e24)
    MARS = (4, 6.417e23)
    JUPITER = (5, 1.898e27)
    SATURN = (6, 5.683e26)
    URANUS = (7, 8.681e25)
    NEPTUNE = (8, 1.024e26)

    def __init__(self, order, mass):
        self.order = order
        self.mass = mass


def calc(a: float, b: float, operator: str) -> float:

    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case _:
            raise ValueError("Invalid operator")





def get_day_of_week(day: int) -> str:
    return {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }.get(day, "Invalid value")



if __name__ == "__main__":
    main()























