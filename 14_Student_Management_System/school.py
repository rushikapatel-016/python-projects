from student import Student
from teacher import Teacher


class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    # --------------------
    # Student Methods
    # --------------------

    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully!")

    def remove_student(self, roll_number):
        try:
            for student in self.students:
                if student.roll_number == roll_number:
                    self.students.remove(student)
                    print("Student removed successfully!")
                    return
            raise ValueError("Student not found.")

        except ValueError as e:
            print(e)

    def search_student(self, roll_number):
        try:
            for student in self.students:
                if student.roll_number == roll_number:
                    student.display_student()
                    return student
            raise LookupError("Student not found.")

        except LookupError as e:
            print(e)

    def display_students(self):
        if len(self.students) == 0:
            print("No students available.")
        else:
            print("\n----- Student List -----")
            for student in self.students:
                student.display_student()
                print("-" * 30)

    # --------------------
    # Teacher Methods
    # --------------------

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print("Teacher added successfully!")

    def display_teachers(self):
        if len(self.teachers) == 0:
            print("No teachers available.")
        else:
            print("\n----- Teacher List -----")
            for teacher in self.teachers:
                teacher.display_teacher()
                print("-" * 30)
