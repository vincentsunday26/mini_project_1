#  Module 2: Mini-project | To-Do list Application


def display_menu():
    print("\nWelcome to the To-Do List App!")
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] += " [X]"
            print(f"Task {task_num} marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                mark_task_complete(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Quitting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
