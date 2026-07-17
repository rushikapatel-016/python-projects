from person import Person


class Teacher(Person):
    def __init__(self, name, age, contact, employee_id, subject, salary):
        super().__init__(name, age, contact)
        self.employee_id = employee_id
        self.subject = subject
        self.salary = salary

    def display_teacher(self):
        self.display_info()
        print(f"Employee ID : {self.employee_id}")
        print(f"Subject     : {self.subject}")
        print(f"Salary      : ₹{self.salary}")
