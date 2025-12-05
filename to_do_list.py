import csv
import os
from datetime import datetime

FILE_NAME = "tasks.csv"


def initialize_csv():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "task", "status", "date_created"])


# To load tasks
def load_tasks():
    tasks = []
    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tasks.append(row)
    return tasks


# To save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "task", "status", "date_created"])
        writer.writeheader()
        writer.writerows(tasks)


# To add a new task
def add_task():
    task = input("Enter task description: ").strip()

    if task == "":
        print("Task cannot be empty!")
        return

    tasks = load_tasks()
    next_id = len(tasks) + 1

    new_task = {
        "id": str(next_id),
        "task": task,
        "status": "Pending",
        "date_created": str(datetime.now().date())
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print("✔ Task added successfully!")


# View tasks in formatted table

def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print("\nID | Task                         | Status   | Date Created")
    print("-" * 60)

    for t in tasks:
        print(f"{t['id']: <3}| {t['task'][:25]: <28}| {t['status']: <8}| {t['date_created']}")


# Mark a task as completed
def mark_task_done():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to update.")
        return

    view_tasks()
    task_id = input("\nEnter task ID to mark as done: ")

    found = False
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "Done"
            found = True
            break

    if not found:
        print("Invalid task ID")
    else:
        save_tasks(tasks)
        print("✔ Task marked as completed!")


# Delete a task
def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks()
    task_id = input("\nEnter task ID to delete: ")

    new_tasks = [t for t in tasks if t["id"] != task_id]

    if len(new_tasks) == len(tasks):
        print(" Invalid task ID")
        return

    # Reassign IDs
    for i, task in enumerate(new_tasks, start=1):
        task["id"] = str(i)

    save_tasks(new_tasks)
    print("✔ Task deleted!")


# Main Menu
def main():
    initialize_csv()

    while True:
        print("\n======== TO-DO LIST MENU ========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        print("=================================")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "_main_":
    main()