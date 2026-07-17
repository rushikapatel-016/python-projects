from school import School
from student import Student
from file_handler import save_students, load_students


school = School()
school.students = load_students()


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Save Data")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        contact = input("Enter Contact: ")
        roll_number = input("Enter Roll Number: ")

        student = Student(name, age, contact, roll_number)

        while True:
            subject = input("Enter Subject (or type 'done' to finish): ")

            if subject.lower() == "done":
                break

            grade = float(input(f"Enter Grade for {subject}: "))
            student.add_subject(subject, grade)

        school.add_student(student)

    elif choice == "2":
        school.display_students()

    elif choice == "3":
        roll_number = input("Enter Roll Number to Search: ")
        school.search_student(roll_number)

    elif choice == "4":
        roll_number = input("Enter Roll Number to Delete: ")
        school.remove_student(roll_number)

    elif choice == "5":
        save_students(school.students)

    elif choice == "6":
        save_students(school.students)
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
