import json
import os
from datetime import datetime
from functools import wraps

# Decorator for logging actions
def log_action(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        action = f"{func.__name__} called with args: {args}, kwargs: {kwargs}"
        print(f"[LOG] {datetime.now()}: {action}")
        result = func(self, *args, **kwargs)
        return result
    return wrapper

class Task:
    def __init__(self, title, description="", priority="medium", completed=False):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = completed
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"], data["description"], data["priority"], data["completed"])
        task.created_at = data["created_at"]
        return task

    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"{status} [{self.priority.upper()}] {self.title}: {self.description}"

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in data]

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    @log_action
    def add_task(self, title, description="", priority="medium"):
        task = Task(title, description, priority)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added.")

    @log_action
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"Task '{removed.title}' removed.")
        else:
            print("Invalid task index.")

    @log_action
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()
            print(f"Task '{self.tasks[index].title}' marked as completed.")
        else:
            print("Invalid task index.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task}")

def main():
    manager = TaskManager()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. List Tasks")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            title = input("Task title: ").strip()
            desc = input("Description: ").strip()
            prio = input("Priority (low/medium/high): ").strip().lower()
            if prio not in ["low", "medium", "high"]:
                prio = "medium"
            manager.add_task(title, desc, prio)
        elif choice == "2":
            index = int(input("Task index to remove: ").strip())
            manager.remove_task(index)
        elif choice == "3":
            index = int(input("Task index to complete: ").strip())
            manager.complete_task(index)
        elif choice == "4":
            manager.list_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
