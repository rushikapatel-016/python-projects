import math_tools
import date_tools
import random_tools

while True:

    print("\n===== PERSONAL UTILITY TOOLKIT =====")
    print("1. Area of Circle")
    print("2. Area of Triangle")
    print("3. Area of Rectangle")
    print("4. Today's Date")
    print("5. Days Until Deadline")
    print("6. Calculate Age")
    print("7. Password Generator")
    print("8. Random Name Picker")
    print("9. Dice Roller")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        radius = float(input("Enter radius: "))
        print("Area of Circle =", round(math_tools.area_circle(radius), 2))

    elif choice == "2":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print("Area of Triangle =", math_tools.area_triangle(base, height))

    elif choice == "3":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print("Area of Rectangle =", math_tools.area_rectangle(length, width))

    elif choice == "4":
        print("Today's Date:", date_tools.today_date())

    elif choice == "5":
        year = int(input("Enter deadline year: "))
        month = int(input("Enter deadline month: "))
        day = int(input("Enter deadline day: "))

        days = date_tools.days_until_deadline(year, month, day)

        if days >= 0:
            print("Days left:", days)
        else:
            print("Deadline has already passed.")

    elif choice == "6":
        birth_year = int(input("Enter birth year: "))
        print("Your age is:", date_tools.calculate_age(birth_year))

    elif choice == "7":
        length = int(input("Enter password length: "))
        print("Generated Password:", random_tools.password_generator(length))

    elif choice == "8":
        names = input("Enter names separated by commas: ").split(",")
        print("Selected Name:", random_tools.random_name_picker(names).strip())

    elif choice == "9":
        print("Dice rolled:", random_tools.dice_roller())

    elif choice == "10":
        print("Thank you for using the Personal Utility Toolkit!")
        break

    else:
        print("Invalid choice! Please try again.")