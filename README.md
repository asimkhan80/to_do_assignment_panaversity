# to_do_assignment_panaversity
# Terminal-based Todo List App

A simple, yet effective, command-line interface (CLI) application for managing your daily tasks. Built entirely in Python, this app provides core to-do list functionalities without leaving the comfort of your terminal.

## Features

- **Add Task**: Quickly add new tasks to your list.
- **List Tasks**: View all your tasks with a clean, color-coded layout. Completed tasks are clearly marked.
- **Update Task**: Edit the title of any existing task.
- **Mark Complete/Incomplete**: Toggle the status of a task between pending and completed.
- **Delete Task**: Remove tasks you no longer need.
- **Persistent Storage**: Your tasks are automatically saved to a `tasks.json` file and reloaded every time you start the app.
- **Error Handling**: The app gracefully handles invalid inputs, such as non-existent task IDs or incorrect menu choices.

## Bonus Features Implemented

- **File Persistence**: Tasks are saved to `tasks.json` on every change (add, update, delete, toggle) and loaded on startup.
- **Colored Output**: The terminal output uses colors to improve user experience, making it easier to distinguish between task statuses and menu options.
- **Clean & Readable CLI**: The output is formatted for clarity, ensuring a pleasant user experience.

## How to Run the App

1.  **Prerequisites**: Ensure you have Python 3.10 or newer installed.
2.  **Navigate**: Open your terminal and navigate to the project directory.
3.  **Run**: Execute the following command:
    ```bash
    python main.py
    ```
4.  **Interact**: Follow the on-screen menu to manage your tasks.

## Folder Structure

```
todo-cli/
│
├── main.py           # Main application entry point, handles UI and user input
├── tasks.py          # Core logic for task manipulation (add, list, update, etc.)
├── storage.py        # Handles loading from and saving to the tasks.json file
├── tasks.json        # Data file for storing tasks (auto-generated)
└── README.md         # This file
```

## How Gemini CLI Helped

Gemini CLI was instrumental in the rapid development of this project. It helped generate the initial project structure, write the complete, ready-to-run code for all modules (`main.py`, `tasks.py`, `storage.py`), implement file persistence using JSON, add colored terminal output for better UX, and structure the final README.md file. This allowed for a quick and efficient development cycle from requirements to a fully functional application.
