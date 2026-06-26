from datetime import date

while True:
    print("\n===== DIARY APP =====")
    print("1. Write a new diary entry")
    print("2. View all diary entries")
    print("3. Count diary entries")
    print("4. Search diary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        entry = input("Write your diary entry: ")

        with open("diary.txt", "a") as file:
            file.write(f"{date.today()} - {entry}\n")

        print("Diary entry saved successfully!")

    elif choice == "2":
        try:
            with open("diary.txt", "r") as file:
                content = file.read()

            if content:
                print("\n----- ALL DIARY ENTRIES -----")
                print(content)
            else:
                print("Diary is empty.")

        except FileNotFoundError:
            print("Diary file not found.")

    elif choice == "3":
        try:
            with open("diary.txt", "r") as file:
                lines = file.readlines()

            print("Total diary entries:", len(lines))

        except FileNotFoundError:
            print("Diary file not found.")

    elif choice == "4":
        keyword = input("Enter keyword to search: ")

        try:
            found = False

            with open("diary.txt", "r") as file:
                for line in file:
                    if keyword.lower() in line.lower():
                        print(line.strip())
                        found = True

            if not found:
                print("No matching diary entry found.")

        except FileNotFoundError:
            print("Diary file not found.")

    elif choice == "5":
        print("Thank you for using the Diary App!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
