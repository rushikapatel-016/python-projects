tasks = []

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task added!\n")

def view_tasks():
    if not tasks:
        print("No tasks found!\n")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task():
    view_tasks()
    try:
        n = int(input("Enter task number to delete: "))
        tasks.pop(n - 1)
        print("Task deleted!\n")
    except:
        print("Invalid input!\n")


while True:
    print("===== TO-DO LIST APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
