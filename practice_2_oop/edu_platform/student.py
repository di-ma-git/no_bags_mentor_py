from participant import Participant


class Student(Participant):
    _progress: {}
    _counter: int = 0


    def __init__(self, name: str):
        self._name = name
        self._progress = {}
        self._id = Student._counter
        Student._counter += 1

    def get_name(self) -> str:
        return self._name

    def get_id(self) -> int:
        return self._id

    def get_progress(self) -> {}:
        return self._progress

    def set_progress(self, course_name, progress):
        if course_name not in self._progress.keys():
            self._progress[course_name] = 1
        else:
            self._progress[course_name] += progress

    def study(self, course_name):
        if course_name not in self._progress.keys():
            self._progress[course_name] = 1
        else:
            self._progress[course_name] += 1

    def show_progress(self, course_name):
        print(f"{course_name}: progress {self._progress[course_name]}")
