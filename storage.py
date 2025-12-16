import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """
    Loads tasks from the JSON file.
    If the file doesn't exist, it returns an empty list.
    """
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r') as f:
            tasks = json.load(f)
            return tasks
    except (json.JSONDecodeError, IOError):
        # If file is empty or corrupted, start with an empty list
        return []

def save_tasks(tasks):
    """
    Saves the list of tasks to the JSON file.
    """
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)
    except IOError as e:
        print(f"Error saving tasks: {e}")

