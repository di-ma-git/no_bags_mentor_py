import random
import string


# Напишите программу, которая удаляет все чётные числа из ArrayList.

arr = [42, 1, 0, -5, 412341]

arr.append(0)

print(arr)

for i in arr:
    if i % 2 == 0:
        arr.remove(i)

print(arr)

# Создайте ArrayList из строк. Найдите в нём самую длинную строку и выведите её.

arr_string = []

for i in range(0, 10):
    arr_string.append(''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 100))))

print(arr_string)

max_str = ""
for i, v in enumerate(arr_string):
    if len(v) > len(max_str):
        max_str = arr_string[i]

print(max_str)


# Создайте ArrayList из целых чисел. Напишите программу, которая вычисляет и выводит сумму всех чисел в списке.

arr_int = []

for i in range(1, 10):
    arr_int.append(random.randint(200, 100000))

print(arr_int)

sum: int = 0
for i in arr_int:
    sum += i

print(sum)

# Создайте ArrayList из целых чисел. Напишите программу, которая находит и выводит максимальное число из списка.
max_int = 0
for i in arr_int:
    if i > max_int:
        max_int = i

print(max_int)


# Дополнительные по желанию:
# Реализуйте метод, который объединяет два ArrayList в один и удаляет дубликаты.


arr_1 = [1, -2, 2, 3, 2, 100]
arr_2 = [3, 4, 5, 100]
arr_3 = arr_1 + arr_2


print(arr_3)

def remove_duplicates(arr: []) -> []:
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result


print(remove_duplicates(arr_3))

# Напишите метод, который принимает ArrayList<Integer> и
# возвращает новый список с числами в отсортированном порядке без использования Collections.sort()
print("===========================")
def sort(arr: []) -> []:
    sort_result = []
    while arr:
        min = arr[0]
        for i in arr:
            if i < min:
                min = i
        sort_result.append(min)
        arr.remove(min)

        print(arr)

    return sort_result


print(arr_3)
print(sort(arr_3))

