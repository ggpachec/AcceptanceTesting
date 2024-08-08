from datetime import datetime

to_do_list = []


def add_task(task, priority='Normal'):
    """Adds a new task to the to-do list with an optional priority."""
    task_data = {
        "task": task,
        "status": "Pending",
        "priority": priority,
        "timestamp": datetime.now()
    }
    to_do_list.append(task_data)
    print(f'Task "{task}" added with priority "{priority}".')


def list_tasks():
    """Prints all tasks in the to-do list."""
    if not to_do_list:
        print("No tasks available.")
    else:
        print("\nAll Tasks:")
        for t in to_do_list:
            print(f'- {t["task"]} [Priority: {t["priority"]}, Status: {t["status"]}]')


def list_top_5_tasks():
    """Prints the top 5 tasks based on priority and timestamp."""
    sorted_tasks = sorted(to_do_list, key=lambda x: (priority_order(x["priority"]), x["timestamp"]))
    print("\nTop 5 Tasks:")
    for task in sorted_tasks[:5]:
        print(f'- {task["task"]} [Priority: {task["priority"]}, Status: {task["status"]}]')


def mark_task_completed(task):
    """Marks a specific task as completed."""
    for t in to_do_list:
        if t["task"] == task:
            t["status"] = "Completed"
            print(f'Task "{task}" marked as completed.')
            return
    print(f'Task "{task}" not found.')


def clear_tasks():
    """Clears all tasks from the to-do list."""
    to_do_list.clear()
    print("All tasks have been cleared.")


def list_tasks_by_priority(priority):
    """Lists all tasks filtered by a given priority."""
    tasks = [t for t in to_do_list if t["priority"] == priority]
    if not tasks:
        print(f"No tasks with priority {priority}.")
    else:
        print(f"\nTasks with {priority} priority:")
        for t in tasks:
            print(f'- {t["task"]} [Status: {t["status"]}]')


def priority_order(priority):
    """Returns a numerical value for priority sorting."""
    priorities = {'High': 1, 'Normal': 2, 'Low': 3}
    return priorities.get(priority, 4)


def show_menu():
    """Displays the menu options to the user."""
    print("\nMenu:")
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. List top 5 tasks")
    print("4. Mark a task as completed")
    print("5. Clear all tasks")
    print("6. List tasks by priority")
    print("7. Exit")


def main():
    """Main function to run the interactive to-do list."""
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            priority = input("Enter the priority (High, Normal, Low): ")
            add_task(task, priority)

        elif choice == '2':
            list_tasks()

        elif choice == '3':
            list_top_5_tasks()

        elif choice == '4':
            task = input("Enter the task to mark as completed: ")
            mark_task_completed(task)

        elif choice == '5':
            confirm = input("Are you sure you want to clear all tasks? (yes/no): ")
            if confirm.lower() == 'yes':
                clear_tasks()

        elif choice == '6':
            priority = input("Enter the priority to filter by (High, Normal, Low): ")
            list_tasks_by_priority(priority)

        elif choice == '7':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
