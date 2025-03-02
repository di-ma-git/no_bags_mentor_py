from participant import Participant
from practice_2_oop.edu_platform.student import Student


class Teacher(Participant):
    _courses: []
    _counter: int = 0


    def __init__(self, name: str):
        self._name = name
        self._courses = []
        self._id = Teacher._counter
        Teacher._counter += 1

    def get_name(self) -> str:
        return self._name

    def get_id(self) -> int:
        return self._id

    def check_task(self, student: Student, course_name: str, progress: int = 1):
        student.set_progress(course_name, progress)

