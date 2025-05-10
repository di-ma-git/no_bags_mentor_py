from math import pi

class Car:
    brand: str
    year: int

    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    def set_brand(self, value: str):
        self.brand = value

    def set_year(self, value: int):
        self.year = value

    def get_brand(self) -> str:
        return self.brand

    def get_year(self) -> int:
        return self.year

    def print(self):
        print(f"Brand: {self.brand}, year of release: {self.year}")


class Rectangle:
    width: float
    height: float

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def set_width(self, val: float):
        self.width = val

    def set_height(self, val: float):
        self.height = val

    def get_width(self) -> float:
        return self.width

    def get_height(self) -> float:
        return self.height

    def calculate_area(self) -> float:
        return self.width * self.height


class Book:
    title: str
    author: str

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def set_title(self, value: str):
        self.title = value

    def set_author(self, value: str):
        self.author = value

    def get_title(self) -> str:
        return self.title

    def get_author(self) -> str:
        return self.author

    def print(self):
        print(f"Title: {self.title}, Author: {self.author}")


class BankAccount:
    owner: str
    balance: float

    def __init__(self, owner: str, bal: float = 0.0):
        self.owner = owner
        self.balance = bal

    def set_owner(self, value: str):
        self.owner = value

    def get_owner(self) -> str:
        return self.owner

    def get_balance(self) -> float:
        return self.balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount

    def print_balance(self):
        print(f"Your balance, {self.owner} is: {self.balance}")


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, val: int):
        self.x = val

    def set_y(self, val: int):
        self.y = val

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def print(self):
        print(f"x = {self.x}, y = {self.y}")

class StudentGroup:
    group_name: str
    student_count: int

    def __init__(self, name: str, count: int):
        self.group_name = name
        self.student_count = count

    def set_group_name(self, name: str):
        self.group_name = name

    def set_student_count(self, count: int):
        self.student_count = count

    def get_group_name(self) -> str:
        return self.group_name

    def get_student_count(self) -> int:
        return self.student_count

    def print_info(self):
        print(f"Group: {self.group_name}, Count of students: {self.student_count}")

class Circle:
    radius: float

    def __init__(self, radius: float):
        self.radius = radius

    def set_radius(self, value: float):
        self.radius = value

    def get_radius(self) -> float:
        return self.radius

    def calc_area(self) -> float:
        return round((pi * self.radius ** 2), 2)

    def calc_circumference(self) -> float:
        return round((2 * pi * self.radius), 2)

class Product:
    name: str
    price: float

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = round(price ,2)

    def set_name(self, value: str):
        self.name = value

    def set_price(self, value: float):
        self.price = value

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def apply_discount(self, discount: float) -> float:
        self.price -= round((self.price / 100 * discount), 2)
        return self.price

    def print_info(self):
        print(f"Good: {self.name}, price: {self.price}")
















