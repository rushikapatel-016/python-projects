expenses = []

def add_expense():
    item = input("Enter item: ")
    amount = float(input("Enter amount: "))
    expenses.append((item, amount))
    print("Expense added!\n")

def view_expenses():
    if not expenses:
        print("No expenses found!\n")
        return

    total = 0
    for i, (item, amount) in enumerate(expenses, 1):
        print(f"{i}. {item} - ₹{amount}")
        total += amount

    print(f"Total Expense: ₹{total}\n")

def delete_expense():
    view_expenses()
    try:
        n = int(input("Enter number to delete: "))
        expenses.pop(n - 1)
        print("Deleted!\n")
    except:
        print("Invalid input!\n")


while True:
    print("===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        break
