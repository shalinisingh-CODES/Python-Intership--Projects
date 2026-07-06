tasks = []

def show_menu():
    print("\n----- TO DO LIST APPLICATION -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    task = input("Enter task: ").strip()

    if task == "":
        print("Task cannot be empty!")
        return

    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added!")


def view_task():
    if not tasks:
        print("No tasks yet!")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✅ DONE" if task["done"] else "❌ NOT DONE"
        print(f"{index}. {task['task']} [{status}]")


def mark_done():
    view_task()

    if not tasks:
        return

    try:
        index = int(input("Enter task number to mark as done: ")) - 1

        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


def delete_task():
    view_task()

    if not tasks:
        return

    try:
        index = int(input("Enter task number to delete: ")) - 1

        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")



while True:
    show_menu()

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_task()

    elif choice == '2':
        view_task()

    elif choice == '3':
        mark_done()

    elif choice == '4':
        delete_task()

    elif choice == '5':
        print("Thank you for using the To-Do List App!")
        break

    else:
        print("Invalid choice! Please try again.")