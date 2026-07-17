from student import Student


def save_students(students, filename="students.txt"):
    try:
        with open(filename, "w") as file:
            for student in students:
                subjects = ",".join(student.subjects)
                grades = ",".join(
                    f"{subject}:{grade}" for subject, grade in student.grades.items()
                )

                file.write(
                    f"{student.name}|{student.age}|{student.contact}|"
                    f"{student.roll_number}|{subjects}|{grades}\n"
                )

        print("Student data saved successfully!")

    except Exception as e:
        print("Error saving data:", e)


def load_students(filename="students.txt"):
    students = []

    try:
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) != 6:
                    continue

                name, age, contact, roll_number, subjects, grades = data

                student = Student(name, int(age), contact, roll_number)

                if subjects:
                    student.subjects = subjects.split(",")

                if grades:
                    for item in grades.split(","):
                        if ":" in item:
                            subject, grade = item.split(":")
                            student.grades[subject] = float(grade)

                students.append(student)

    except FileNotFoundError:
        print("No existing student data found.")

    except Exception as e:
        print("Error loading data:", e)

    return students
