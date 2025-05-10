from course import Course
from manager import Manager
from teacher import Teacher
from student import Student


def main():

    vitya = Student("Student Vitya")
    kostya = Student("Student Kostya")
    petya = Student("Student Petr")

    prepod = Teacher("Vasiliy Dmitrich")

    course_python = Course("Python programming")

    course_python.add_student(vitya)
    course_python.add_student(kostya)
    course_python.add_student(petya)
    course_python.add_teacher(prepod)

    course_python.show_all_participants()

    vitya.study(course_python.get_name())
    vitya.study(course_python.get_name())
    vitya.study(course_python.get_name())

    prepod.check_task(vitya, course_python.get_name())
    prepod.check_task(vitya, course_python.get_name(), 5)

    vitya.show_progress(course_python.get_name())

    manager = Manager()

    dima = Student("Student Dima")
    prepod2 = Teacher("Timur Andreevich")
    java = Course("Java programming")

    manager.assign_to_course(dima, java)
    manager.assign_to_course(prepod2, java)



if __name__ == "__main__":
    main()