from turtledemo.forest import doit1

from conditions import get_number


def main():

    # Напишите программу, которая запрашивает у пользователя число и продолжает запрашивать,
    # пока введённое число не станет положительным.
    k: int = 0
    while k <= 0:
        try:
            k = int(get_number())
            if k > 0:
                print("Eventually, your number turned positive.")
                break
            else:
                print("Please, enter a positive number")
        except ValueError as e:
            print(f"Error: an incorrect number was entered <<{str(e.args)}>>")

    # Реализуйте программу, которая запрашивает у пользователя пароль,
    # пока он не введёт верный (заданный заранее).
    passw: str = ""
    while passw != "11223344":
        print("Enter your password")
        passw = get_number()
        if passw == "11223344":
            print("You logged in")
            break
        else:
            print("Wrong password")

    # Создайте программу, которая выводит числа от 1 до 10, но использует цикл do-while.
    i: int = 0
    while True:
        i += 1
        print(i)
        if i == 10:
            break

    # Напишите программу, которая запрашивает числа у пользователя и выводит их сумму.
    # Если пользователь вводит отрицательное число, программа завершает выполнение (break).
    summa: float = 0
    while True:
        try:
            user_input = float(get_number())
            if user_input < 0:
                print("The application was closed")
                break
            summa += user_input
            print(f"Sum is: {summa}")
        except ValueError:
            print("Invalid value")

    # Создайте программу, которая выводит числа от 1 до 20,
    # пропуская те, которые делятся на 3 (continue).
    num: int = 0
    while True:
        num += 1
        if (num % 3) == 0: continue
        if num > 20:
            break
        print(num)

    # Реализуйте программу, которая выводит первые 10 чисел,
    # которые одновременно делятся на 2 и 5. Используйте break для завершения цикла, когда будет найдено 10 чисел.
    count: int = 0
    num: int = 0
    while count < 10:
        num += 1
        if num % 2 == 0 and num % 5 == 0:
            count += 1
            print(f"{count}. {num}")







if __name__ == "__main__":
    main()


































