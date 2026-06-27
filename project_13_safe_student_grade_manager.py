def add_student():
    try:
        name = input("Enter student name: ")

        grade = float(input("Enter grade (0-100): "))

        if grade < 0 or grade > 100:
            raise ValueError

        with open("grades.txt", "a") as file:
            file.write(f"{name},{grade}\n")

        print("Student grade saved successfully.")

    except ValueError:
        print("Error: Grade must be a number between 0 and 100.")


def display_grades():
    try:
        with open("grades.txt", "r") as file:
            data = file.readlines()

        if len(data) == 0:
            print("No grades available.")
            return

        print("\n----- Student Grades -----")

        for line in data:
            name, grade = line.strip().split(",")
            print(f"Name: {name} | Grade: {grade}")

    except FileNotFoundError:
        print("grades.txt not found.")


def calculate_average():
    try:
        with open("grades.txt", "r") as file:
            data = file.readlines()

        if len(data) == 0:
            print("No grades available to calculate average.")
            return

        total = 0

        for line in data:
            name, grade = line.strip().split(",")
            total += float(grade)

        average = total / len(data)

        print(f"Class Average: {average:.2f}")

    except FileNotFoundError:
        print("grades.txt not found.")

    except ZeroDivisionError:
        print("No grades found.")


def search_student():
    try:
        student = input("Enter student name to search: ")

        with open("grades.txt", "r") as file:
            data = file.readlines()

        found = False

        for line in data:
            name, grade = line.strip().split(",")

            if name.lower() == student.lower():
                print(f"{name}'s Grade: {grade}")
                found = True
                break

        if not found:
            print("Student not found.")

    except FileNotFoundError:
        print("grades.txt not found.")


while True:

    print("\n===== SAFE STUDENT GRADE MANAGER =====")
    print("1. Add Student Grade")
    print("2. Display All Grades")
    print("3. Calculate Class Average")
    print("4. Search Student Grade")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_grades()

    elif choice == "3":
        calculate_average()

    elif choice == "4":
        search_student()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")