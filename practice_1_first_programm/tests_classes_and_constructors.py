from classes_and_constructors import Car, Rectangle, Book, BankAccount
from practice_1_first_programm.classes_and_constructors import Point, StudentGroup, Circle, Product


def test_class_car():

    bmw = Car("BMW", 2024)
    bmw.print()

    assert bmw.brand == "BMW"
    assert bmw.year == 2024

def test_class_rectangle():

    rectangle = Rectangle(5.15, 6.16)
    rectangle.set_width(7.17)
    square = rectangle.calculate_area()

    assert square == (7.17 * 6.16)

def test_class_book():

    harry = Book("Harry Potter", "John Rolling")
    harry.print()

    assert harry.title == "Harry Potter"
    assert harry.author == "John Rolling"

def test_class_bank_account():
    client_sasha = BankAccount("Alexandr")
    client_dima = BankAccount("Dmitry", -500.50)

    client_sasha.deposit(450)
    client_dima.deposit(1000.25)
    client_sasha.withdraw(50.15)

    client_sasha.print_balance()
    client_dima.print_balance()

    assert client_sasha.get_owner() == "Alexandr"
    assert client_sasha.get_balance() == 399.85
    assert client_dima.get_owner() == "Dmitry"
    assert client_dima.get_balance() == 499.75

def test_class_point():
    point = Point(100, 200)
    point.set_x(300)

    point.print()

    assert point.get_x() == 300

def test_class_student_group():
    group = StudentGroup("QA", 30)
    group.set_student_count(34)

    group.print_info()

    assert group.get_group_name() == "QA"
    assert group.get_student_count() == 34

def test_class_circle():
    circ = Circle(5555.22)
    circ.set_radius(3333.33)

    area = circ.calc_area()
    circumference = circ.calc_circumference()

    assert  area == 34906515.23
    assert  circumference == 20943.93

def test_class_product():
    bread = Product("Bread", 15.99)
    bread.apply_discount(5)

    bread.print_info()

    assert bread.get_price() == 15.19















