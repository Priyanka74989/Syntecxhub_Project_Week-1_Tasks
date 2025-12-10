import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    """Load tasks from JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    print("\n--- Add New Task ---")
    title = input("Task title: ")

    # Optional (extra credit)
    tag = input("Tag (optional): ").strip()
    due = input("Due date (optional): ").strip()

    task = {
        "title": title,
        "done": False,
        "tag": tag if tag else None,
        "due": due if due else None
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def view_tasks(tasks):
    print("\n------ Your Tasks ------")

    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        extra = ""

        if task.get("tag"):
            extra += f"  [Tag: {task['tag']}]"
        if task.get("due"):
            extra += f"  [Due: {task['due']}]"

        print(f"{i + 1}. {status} {task['title']}{extra}")

def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        idx = int(input("\nEnter task number to mark done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            save_tasks(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        idx = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n======= To-Do List Manager =======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()