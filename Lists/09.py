pending_tasks = []
completed_tasks = []

def add_task():
    task = input("Enter the task: ")
    pending_tasks.append(task)
    print(f"Task '{task}' added successfully!\n")

def mark_completed():
    if not pending_tasks:
        print("No pending tasks to complete!\n")
        return
    view_tasks(pending_tasks, "Pending")
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(pending_tasks):
            completed_tasks.append(pending_tasks.pop(index))
            print("Task marked as completed!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

def view_tasks(task_list, task_type):
    if not task_list:
        print(f"No {task_type.lower()} tasks available.\n")
        return
    print(f"\n{task_type} Tasks:")
    for i, task in enumerate(task_list, start=1):
        print(f"{i}. {task}")
    print()

def main():
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Pending Tasks")
        print("4. View Completed Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            mark_completed()
        elif choice == '3':
            view_tasks(pending_tasks, "Pending")
        elif choice == '4':
            view_tasks(completed_tasks, "Completed")
        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.\n")

main()
