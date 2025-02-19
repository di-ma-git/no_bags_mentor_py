from http.client import UnimplementedFileMode
from itertools import count
from random import randint


class Company:
    company_name: str
    __counter: int = 1


    def __init__(self, name: str):
        self.employee_name = name
        self.__employee_id = Company.__counter
        Company.__counter += 1

    def set_employee_name(self, name: str):
        self.employee_name = name

    @property
    def get_employee_id(self) -> int:
        return self.__employee_id

    def get_employee_name(self) -> str:
        return self.employee_name

    def print_company_name(self):
        print(Company.company_name)


class MathConstants:
    __PI: float = 3.14159
    __E: float = 2.71828

    @staticmethod
    def get_pi() -> float:
        return MathConstants.__PI

    @staticmethod
    def get_e() -> float:
        return MathConstants.__E

    @staticmethod
    def calc_circle_area(rad: float) -> float:
        return MathConstants.__PI * rad ** 2

    @staticmethod
    def calc_circumference(rad: float) -> float:
        return 2 * MathConstants.__PI * rad


class Library:
    __book_title: str
    _author: str
    year: int
    category: str


    @property
    def book_title(self) -> str:
        return self.__book_title

    @property
    def author(self) -> str:
        return self._author

    def get_year(self) -> int:
        return self.year

    def get_category(self) -> str:
        return self.category

    @book_title.setter
    def book_title(self, value: str):
        self.__book_title = value

    @author.setter
    def author(self, value: str):
        self._author = value

    def set_year(self, value: int):
        self.year = value

    def set_category(self, value: str):
        self.category = value

class University:
    university_name: str
    __counter: int = 1
    __student_id: int
    student_name: str

    def __init__(self, student_name: str):
        self.student_name = student_name
        self.__student_id = University.__counter
        University.__counter += 1

    @property
    def student_id(self) -> int:
        return self.__student_id

    def get_student_name(self) -> str:
        return self.student_name

    def print_student_info(self):
        print(f"University: {University.university_name}, student: {self.student_name}")

    @staticmethod
    def change_university_name(new_name: str):
        University.university_name = new_name

class GameSettings:
    __max_players: int # static
    __game_name: str # final
    current_players: int = 0

    def __init__(self, game_name: str, current_number: int):
        self.__game_name = game_name
        self.current_players = current_number

    @property
    def game_name(self) -> str:
        return self.__game_name

    @staticmethod
    def set_max_players(value: int):
        GameSettings.__max_players = value

    def add_player(self):
        if self.current_players < GameSettings.__max_players:
            self.current_players += 1
        else:
            raise RuntimeError("The maximum number of players has been reached")

    def print_game_status(self):
        print(f"Game: {self.__game_name}, "
              f"current number of players: {self.current_players}, "
              f"max number of players: {GameSettings.__max_players}")


class Person:
    __first_name: str
    __last_name: str
    __ssn: str

    def __init__(self, first_name: str, last_name: str, ssn: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__ssn = ssn

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def ssn(self) -> str:
        return self.__ssn

    @first_name.setter
    def first_name(self, val: str):
        self.__first_name = val

    @last_name.setter
    def last_name(self, val: str):
        self.__last_name = val

    def print_person_info(self):
        print(f"Name: {self.__first_name}, Surname: {self.__last_name}, SSN: {self.__ssn}")








