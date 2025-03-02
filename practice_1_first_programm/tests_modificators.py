import pytest

from modificators import Company, MathConstants, Library, University, GameSettings, Person


def test_company():
    Company.company_name = "Google"

    empl1 = Company("Semen")
    empl2 = Company("Petr")
    empl3 = Company("John")

    empl1.print_company_name()
    empl2.print_company_name()
    empl3.print_company_name()

    assert empl1.get_employee_id == 1
    assert empl2.get_employee_id == 2
    assert empl3.get_employee_id == 3

    Company.company_name = "Microsoft"

    empl1.print_company_name()
    empl2.print_company_name()
    empl3.print_company_name()

def test_company_private_attribute_protection():
    Company.company_name = "Google"

    empl1 = Company("Semen")

    with pytest.raises(AttributeError) as e:
        _ = empl1.__employee_id

    assert "object has no attribute '__employee_id'" in  str(e.value)

def test_math_constant():
    assert MathConstants.get_pi() == 3.14159
    assert MathConstants.get_e() == 2.71828

    a = MathConstants.calc_circle_area(5)
    b = MathConstants.calc_circumference(6)

    assert round(a, 5) == 78.53975
    assert round(b, 5) == 37.69908

def test_library():
    lib = Library()

    lib.book_title = "Brave New World"
    lib.author = "Aldous Huxley"
    lib.set_year(1931)
    lib.set_category("Fiction")

    assert lib.book_title == "Brave New World"
    assert lib.author == "Aldous Huxley"
    assert lib.get_year() == 1931
    assert lib.get_category() == "Fiction"

def test_university():
    student1 = University("Kolya")
    student2 = University("Vanya")
    student3 = University("Artem")

    University.change_university_name("VGGU")

    student1.print_student_info()
    student2.print_student_info()
    student3.print_student_info()

def test_game_settings():
    wow = GameSettings("Wow", 10)
    football = GameSettings("Football", 5)

    GameSettings.set_max_players(15)

    wow.print_game_status()
    football.print_game_status()

    wow.add_player()
    wow.add_player()
    wow.add_player()
    wow.add_player()
    wow.add_player()
    football.add_player()
    football.add_player()
    football.add_player()

    wow.print_game_status()
    football.print_game_status()

def test_maximum_number_of_players():
    wow = GameSettings("Wow", 10)
    GameSettings.set_max_players(15)
    wow.add_player()
    wow.add_player()
    wow.add_player()
    wow.add_player()
    wow.add_player()

    with pytest.raises(RuntimeError) as e:
        wow.add_player()

    assert e.value.args[0] == "The maximum number of players has been reached"

def test_person():
    tom = Person("Tom", "Ford", "333")
    yves = Person("Yves", "Saint Laurent", "444")
    christian = Person("Christian", "Dior", "555")
    hugo = Person("Hugo", "Boss", "666")


    tom.last_name = "Hardy"

    tom.print_person_info()
    yves.print_person_info()
    christian.print_person_info()
    hugo.print_person_info()

def test_person_try_to_change_final_attribute():
    tom = Person("Tom", "Ford", "333")

    try:
        tom.ssn = "xxx"
    except AttributeError:
        print("SSN нельзя изменить!")





