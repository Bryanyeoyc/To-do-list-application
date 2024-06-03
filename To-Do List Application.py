tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'Task "{removed_task}" removed.')
    else:
        print("Invalid task number.")

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
