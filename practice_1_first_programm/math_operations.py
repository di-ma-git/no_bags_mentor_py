import math


class MathOperations:



    def add(self, x: int, y: int) -> int:
        return x + y

    def subtract(self, x: int, y: int) -> int:
        return x - y

    def multiply(self, x: int, y: int) -> int:
        return x * y

    def divide(self, x: int, y: int) -> float:
        if y == 0:
            raise ZeroDivisionError("It doesn't allow dividing by zero")
        else:
            return x / y

    def find_max(self, a: int, b: int) -> int:
        return max(a, b)

    def square_area(self, side: int) -> int:
        if side <= 0:
            raise ValueError("Invalid value")
        return side ** 2

    def square_perimeter(self, side: int) -> int:
        if side <= 0:
            raise ValueError("Invalid value")
        return side * 4

    def convert_second_to_minutes(self, seconds: int) -> str:
        if seconds < 0:
            raise ValueError("Second can't be negative")
        return f"{seconds // 60} minutes, {seconds % 60} seconds"

    def average_speed(self, distance: float, time: float) -> str:
        for  i in [distance, time]:
            if i <= 0:
                raise ValueError("The value can't be less then or equal to zero")
        return f"The speed is {(distance / time):.2f} meters/second"

    def find_hypotenuse(self, a: float, b: float) -> float:
        if a <= 0 or b <= 0:
            raise ValueError("Invalid value")
        return math.sqrt((a ** 2) + (b ** 2))

    def calculate_percentage(self, total: float, part: float) -> float:
        if total <= 0 or part <= 0 or total < part:
            raise ValueError("Invalid value")
        return round((part / total * 100), 6)

    def celsius_to_fahrenheit(self, celsius: float) -> float:
        if celsius < -273.15:
            raise ValueError("Invalid value")
        fahrenheit = round(((celsius * 9 / 5) + 32), 1)
        return fahrenheit

    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        if fahrenheit < -459.67:
            raise ValueError("Invalid value")
        celsius = round(((fahrenheit - 32) * 5 / 9), 1)
        return celsius