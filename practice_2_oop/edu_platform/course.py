from practice_2_oop.edu_platform.student import Student
from practice_2_oop.edu_platform.teacher import Teacher


class Course:
    _name: str
    _students: {}
    _teachers: {}

    def __init__(self, name: str):
        self._name = name
        self._students = {}
        self._teachers = {}

    def add_student(self, student: Student):
        if student.get_id not in self._students.keys():
            self._students[student.get_id] = student
        else: print(f"Student with id {student.get_id} is already enrolled in the course")

    def add_teacher(self, teacher: Teacher):
        if teacher.get_id not in self._teachers.keys():
            self._teachers[teacher.get_id] = teacher
        else: print(f"Teacher with id {teacher.get_id} is already assigned to the course")

    def get_name(self) -> str:
        return self._name

    def show_all_participants(self):
        print("Teachers")
        for teacher in self._teachers.values():
            print(f"{teacher.get_id()}. {teacher.get_name()}")
        print("Students")
        for student in self._students.values():
            print(f"{student.get_id()}. {student.get_name()}")