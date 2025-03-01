from participant import Participant
from course import Course
from teacher import Teacher


class Manager:


    def assign_to_course(self, participant: Participant, course: Course):
        if isinstance(participant, Teacher):
            course.add_teacher(participant)
        else:
            course.add_student(participant)

        course.show_all_participants()


