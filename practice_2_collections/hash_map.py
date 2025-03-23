
from typing import Dict
# import collections

# Создайте HashMap<String, Integer>, добавьте 5 пар (имя – возраст) и выведите все записи.
name_age_dict: dict[str, int] = {}


name_age_dict['kate'] = 22
name_age_dict['semen'] = 25
name_age_dict['vasya'] = 30
name_age_dict['petr'] = 44
name_age_dict['dima'] = 11
name_age_dict['vitasik'] = 9

print(name_age_dict)

for k, v in name_age_dict.items():
    print(f"name:{k}, age:{v}")

# Проверьте, есть ли определённое имя в HashMap.


def check_contains_name(name_dict: dict, name1: str) -> str:
    for name, age in name_dict.items():
        if name == name1:
            return f"{name} found, age: {age}"

    return "Not found"


print(check_contains_name(name_age_dict, "sveta"))
print(check_contains_name(name_age_dict, "semen"))
print(check_contains_name(name_age_dict, "vitasik"))


# Реализуйте метод, который печатает из HashMap всех пользователей младше 18 лет.


def is_younger_18(some_dict: dict[str, int]):
    for name, age in some_dict.items():
        if age < 18:
            print(f"{name}. {age}")


is_younger_18(name_age_dict)






