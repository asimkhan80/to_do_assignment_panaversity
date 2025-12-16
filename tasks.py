import storage

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def _get_next_id(tasks):
    """Returns the next available ID for a new task."""
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def _find_task_by_id(tasks, task_id):
    """Finds a task by its ID."""
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

def add_task(tasks, title):
    """
    Adds a new task to the list.
    """
    if not title:
        print(f"{Colors.FAIL}Task title cannot be empty.{Colors.ENDC}")
        return tasks

    new_task = {
        "id": _get_next_id(tasks),
        "title": title,
        "done": False
    }
    tasks.append(new_task)
    storage.save_tasks(tasks)
    print(f"{Colors.OKGREEN}Task added successfully.{Colors.ENDC}")
    return tasks

def list_tasks(tasks):
    """
    Lists all tasks, with colors indicating their status.
    """
    if not tasks:
        print(f"{Colors.WARNING}No tasks found.{Colors.ENDC}")
        return

    print(f"\n{Colors.HEADER}{Colors.BOLD}--- ALL TASKS ---{Colors.ENDC}")
    for task in sorted(tasks, key=lambda k: k['id']):
        status_icon = f"{Colors.OKGREEN}[x]{Colors.ENDC}" if task['done'] else f"{Colors.WARNING}[ ]{Colors.ENDC}"
        task_id_color = Colors.OKBLUE if task['done'] else Colors.BOLD
        print(f"{status_icon} {task_id_color}ID: {task['id']}{Colors.ENDC} - {task['title']}")
    print(f"{Colors.HEADER}{Colors.BOLD}-----------------{Colors.ENDC}\n")


def toggle_task_status(tasks, task_id):
    """
    Marks a task as complete or incomplete.
    """
    task = _find_task_by_id(tasks, task_id)
    if task:
        task['done'] = not task['done']
        storage.save_tasks(tasks)
        status_text = "complete" if task['done'] else "incomplete"
        print(f"{Colors.OKGREEN}Task ID {task_id} marked as {status_text}.{Colors.ENDC}")
    else:
        print(f"{Colors.FAIL}Error: Task with ID {task_id} not found.{Colors.ENDC}")
    return tasks

def update_task(tasks, task_id, new_title):
    """
    Updates the title of an existing task.
    """
    if not new_title:
        print(f"{Colors.FAIL}New title cannot be empty.{Colors.ENDC}")
        return tasks

    task = _find_task_by_id(tasks, task_id)
    if task:
        task['title'] = new_title
        storage.save_tasks(tasks)
        print(f"{Colors.OKGREEN}Task ID {task_id} updated successfully.{Colors.ENDC}")
    else:
        print(f"{Colors.FAIL}Error: Task with ID {task_id} not found.{Colors.ENDC}")
    return tasks

def delete_task(tasks, task_id):
    """
    Deletes a task from the list.
    """
    task = _find_task_by_id(tasks, task_id)
    if task:
        tasks.remove(task)
        storage.save_tasks(tasks)
        print(f"{Colors.OKGREEN}Task ID {task_id} deleted successfully.{Colors.ENDC}")
    else:
        print(f"{Colors.FAIL}Error: Task with ID {task_id} not found.{Colors.ENDC}")
    return tasks
