import tasks
import storage
from tasks import Colors

def print_menu():
    """Prints the main menu of the application."""
    print(f"\n{Colors.HEADER}==== TODO APP ===={Colors.ENDC}")
    print(f"{Colors.OKBLUE}1. Add task{Colors.ENDC}")
    print(f"{Colors.OKBLUE}2. List tasks{Colors.ENDC}")
    print(f"{Colors.OKBLUE}3. Mark task complete/incomplete{Colors.ENDC}")
    print(f"{Colors.OKBLUE}4. Update task{Colors.ENDC}")
    print(f"{Colors.OKBLUE}5. Delete task{Colors.ENDC}")
    print(f"{Colors.WARNING}0. Exit{Colors.ENDC}")
    print(f"{Colors.HEADER}=================={Colors.ENDC}")

def get_task_id_input(prompt):
    """Safely gets and validates a task ID from the user."""
    while True:
        try:
            task_id_str = input(prompt)
            return int(task_id_str)
        except ValueError:
            print(f"{Colors.FAIL}Invalid input. Please enter a valid number for the task ID.{Colors.ENDC}")

def main():
    """Main function to run the CLI application."""
    tasks_list = storage.load_tasks()

    while True:
        print_menu()
        choice = input(f"Enter your choice ({Colors.BOLD}0-5{Colors.ENDC}): ")

        if choice == '1':
            title = input("Enter the task title: ").strip()
            tasks_list = tasks.add_task(tasks_list, title)
        
        elif choice == '2':
            tasks.list_tasks(tasks_list)

        elif choice == '3':
            if not tasks_list:
                print(f"{Colors.WARNING}No tasks to mark. Add a task first.{Colors.ENDC}")
                continue
            tasks.list_tasks(tasks_list)
            task_id = get_task_id_input("Enter the ID of the task to toggle its status: ")
            tasks_list = tasks.toggle_task_status(tasks_list, task_id)

        elif choice == '4':
            if not tasks_list:
                print(f"{Colors.WARNING}No tasks to update. Add a task first.{Colors.ENDC}")
                continue
            tasks.list_tasks(tasks_list)
            task_id = get_task_id_input("Enter the ID of the task to update: ")
            new_title = input("Enter the new title for the task: ").strip()
            tasks_list = tasks.update_task(tasks_list, task_id, new_title)

        elif choice == '5':
            if not tasks_list:
                print(f"{Colors.WARNING}No tasks to delete. Add a task first.{Colors.ENDC}")
                continue
            tasks.list_tasks(tasks_list)
            task_id = get_task_id_input("Enter the ID of the task to delete: ")
            tasks_list = tasks.delete_task(tasks_list, task_id)

        elif choice == '0':
            print(f"{Colors.OKGREEN}Thank you for using the Todo App. Goodbye!{Colors.ENDC}")
            break

        else:
            print(f"{Colors.FAIL}Invalid choice. Please select a valid option from the menu.{Colors.ENDC}")

if __name__ == "__main__":
    main()