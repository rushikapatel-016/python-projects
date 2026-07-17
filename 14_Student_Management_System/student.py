from person import Person


class Student(Person):
    def __init__(self, name, age, contact, roll_number):
        super().__init__(name, age, contact)
        self.roll_number = roll_number
        self.subjects = []
        self.grades = {}

    def add_subject(self, subject, grade):
        self.subjects.append(subject)
        self.grades[subject] = grade

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0

        total = sum(self.grades.values())
        return total / len(self.grades)

    def display_student(self):
        self.display_info()
        print(f"Roll Number : {self.roll_number}")
        print(f"Subjects    : {self.subjects}")
        print(f"Grades      : {self.grades}")
        print(f"Average     : {self.calculate_average():.2f}")
