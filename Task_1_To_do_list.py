import json
import os
from datetime import datetime


TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {
        'title': title,
        'description': description,
        'created_at': datetime.now().isoformat(),
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def update_task(tasks):
    list_tasks(tasks)
    task_id = int(input("Enter task ID to update: "))
    if 0 <= task_id < len(tasks):
        tasks[task_id]['title'] = input("Enter new task title: ")
        tasks[task_id]['description'] = input("Enter new task description: ")
        save_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Invalid task ID")

def delete_task(tasks):
    list_tasks(tasks)
    task_id = int(input("Enter task ID to delete: "))
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task ID")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{i}. {task['title']} - {task['description']} [{status}] (Created at: {task['created_at']})")

def mark_task_complete(tasks):
    list_tasks(tasks)
    task_id = int(input("Enter task ID to mark as complete: "))
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed successfully!")
    else:
        print("Invalid task ID")

def main():
    tasks = load_tasks()
    while True:
        print("Welcome to dhivya's Todo list")
        print("\nTo-Do List Application")
        print("1. Add a Task")
        print("2. Update a Task")
        print("3. Delete a Task")
        print("4. List the Tasks")
        print("5. Mark the Task as Complete")
        print("6. Exit from the application")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            update_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            list_tasks(tasks)
        elif choice == '5':
            mark_task_complete(tasks)
        elif choice == '6':
            break
        else:
            print("Invalid choice.try again later.")

if __name__ == "__main__":
    main()
