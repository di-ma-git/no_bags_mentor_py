from conditions import get_number


def main():
    # Напишите программу, которая выводит все числа от 1 до 100, которые делятся на 3
    print_multiples_of_3()

    # Реализуйте программу, которая принимает с консоли число n
    # и вычисляет сумму всех чисел от 1 до n (включительно)
    print(sum_n(int(get_number())))

    # Создайте программу, которая выводит таблицу умножения для числа, введённого пользователем
    multiply_table(int(get_number()))

def multiply_table(x: int):
    for i in range(1, x + 1):
        print(f"{i} * {x} = {i * x}")

def print_multiples_of_3():
    for i in range(1, 100):
        if i % 3 == 0:
            print(i)


def sum_n(n: int) -> int:
    _sum = 0
    for i in range(1, n + 1):
        _sum += i
    return _sum


if __name__ == "__main__":
    main()