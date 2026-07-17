class Person:
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact

    def display_info(self):
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Contact : {self.contact}")
