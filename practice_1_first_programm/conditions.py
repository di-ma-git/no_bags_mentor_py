


def main():

    # Напишите программу, которая принимает с консоли число и проверяет
    # число положительное, отрицательное, равно нулю
    number = int(get_number())

    if number > 0:
        print(f"Your number {number} is positive")
    elif number < 0:
        print(f"Your number {number} is negative")
    else:
        print(f"Your number {number} is 0")

    # Создайте программу, которая принимает два числа и выводит наибольшее из них
    num1 = float(input("Input first number: "))
    num2 = float(input("Input second number: "))

    print("Max number is: " + str(max_number(num1, num2)))

    num3 = float(get_number())
    num4 = float(get_number())

    print("Max number is: " + str(find_max(num3, num4)))

    # Напишите программу, которая принимает с консоли оценку (1–5) и выводит
    # 5 — "Отлично",
    # 4 — "Хорошо",
    # 3 — "Удовлетворительно",
    # 2 или 1 — "Неудовлетворительно".

    print("Your mark is: " + get_mark(int(get_number())))


def get_mark(mark: int) -> str:
    return {
        5 : "Отлично",
        4 : "Хорошо",
        3 : "Отлично",
        2 : "Удовлетворительно",
        1 : "Удовлетворительно"
    }.get(mark, "Invalid value")

find_max = lambda a, b: a if a > b else b


def max_number(a: float, b: float) -> float:
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a



def get_number() -> str:
    return input("Input your number: ")


if __name__ == "__main__":
    main()