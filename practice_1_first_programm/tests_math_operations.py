from logging import raiseExceptions
from math import sqrt
from sys import orig_argv

import pytest

from math_operations import MathOperations
from random import Random

rnd = Random()
calc = MathOperations()

def test_add():

    for _ in range(1_000_000):

        a = rnd.randint(-1000, 1000)
        b = rnd.randint(-1000, 1000)

        actual_result = calc.add(a, b)

        assert actual_result == (a + b)


def test_subtract():

    for _ in range(1_000_000):

        a = rnd.randint(-1000, 1000)
        b = rnd.randint(-1000, 1000)

        actual_result = calc.subtract(a, b)

        assert actual_result == (a - b)


def test_multiply():

    for _ in range(1_000_000):

        a = rnd.randint(-1000, 1000)
        b = rnd.randint(-1000, 1000)

        actual_result = calc.multiply(a, b)

        assert actual_result == (a * b)


def test_divide():

    for _ in range(1_000_000):

        a = rnd.randint(-1000, 1000)
        b = rnd.randint(-1000, 1000) or rnd.choice((-1, 1))

        actual_result = calc.divide(a, b)

        assert actual_result == pytest.approx(a / b)


def test_divide_by_zero():

    a = rnd.randint(-1000, 1000)
    b = 0

    with pytest.raises(ZeroDivisionError) as exc:
        calc.divide(a, b)

    assert exc.value.args[0] == "It doesn't allow dividing by zero"


@pytest.mark.parametrize("a, b, exp", [
    (10, 11, 11),
    (-600, 0, 0),
    (3, 1, 3),
    (155230, 3213, 155230),
    (0, 0, 0)
])
def test_max(a: int, b: int, exp: int):

    actual_result = calc.find_max(a, b)

    assert actual_result == exp


def test_square_area():

    for _ in range(1_000_000):

        side = rnd.randint(1, 1000)

        actual_result = calc.square_area(side)

        assert actual_result == side ** 2


    with pytest.raises(ValueError) as exc:
        calc.square_area(0)

    assert exc.value.args[0] == "Invalid value"



def test_square_perimeter():

    for _ in range(1_000_000):

        side = rnd.randint(1, 1000)

        actual_result = calc.square_perimeter(side)

        assert actual_result == side * 4

    with pytest.raises(ValueError) as exc:
        calc.square_perimeter(0)

    assert exc.value.args[0] == "Invalid value"

@pytest.mark.parametrize("seconds, minutes", [
    (0, "0 minutes, 0 seconds"),
    (60, "1 minutes, 0 seconds"),
    (12346, "205 minutes, 46 seconds"),
])
def test_convert_seconds_to_minutes(seconds: int, minutes: str):

    actual_result = calc.convert_second_to_minutes(seconds)

    assert actual_result == minutes

    with pytest.raises(ValueError) as exc:
        calc.convert_second_to_minutes(-1)

    assert exc.value.args == ("Second can't be negative",)


@pytest.mark.parametrize("dist, time, speed", [
    (1000, 100, "The speed is 10.00 meters/second"),
    (55, 0.33, "The speed is 166.67 meters/second"),
    (412341, 331, "The speed is 1245.74 meters/second")
])
def test_average_speed(dist: float, time: float, speed: str):

    actual_result = calc.average_speed(dist, time)

    assert actual_result == speed

    with pytest.raises(ValueError) as exc:
        calc.average_speed(-1, 6.66)

    assert exc.value.args == ("The value can't be less then or equal to zero",)


def test_find_hypotenuse():

    for _ in range(1_000_000):

        a = round((0.01 + rnd.random() * 999.98), 2)
        b = round((0.01 + rnd.random() * 999.98), 2)

        actual_result = calc.find_hypotenuse(a, b)

        assert actual_result == sqrt((a ** 2) + (b ** 2))

    with pytest.raises(ValueError) as exc:
        calc.find_hypotenuse(-1, 6.66)

    assert exc.value.args == ("Invalid value",)

@pytest.mark.parametrize("total, part, ", [
    (100, 100),
    (0.000011, 0.000001),
    (300, 5.55),
    (1, 0.99999),
    (34234, 100)
])
def test_calculate_percentage(total: float, part: float):

    actual_result = calc.calculate_percentage(total, part)

    assert actual_result == round((part / total * 100), 6)

def test_calculate_percentage_exception():

    cases = [
        (1, 5, "Invalid value"),
        (0, 5, "Invalid value"),
        (1, 0, "Invalid value"),
        (-1, 5, "Invalid value")
    ]

    for total, part, msg in cases:
        with pytest.raises(ValueError) as e:
            calc.calculate_percentage(total, part)
        assert e.value.args[0] == msg

def test_celsius_to_fahrenheit():
    cases = [
        (333, 631.4),
        (-3, 26.6),
        (-273.1, -459.6),
        (0, 32)
    ]

    for cel, fah in cases:
        assert calc.celsius_to_fahrenheit(cel) == fah

def test_fahrenheit_to_celsius():
    cases = [
        (631.4, 333),
        (26.6, -3),
        (-459.6, -273.1),
        (32, 0)
    ]

    for cel, fah in cases:
        assert calc.fahrenheit_to_celsius(cel) == fah
