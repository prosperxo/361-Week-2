import json
import os

# Dictionary to store tasks for each user
user_tasks = {}

# Function to load user data
def load_user_data():
    if os.path.exists('user_data.json'):
        with open('user_data.json', 'r') as file:
            return json.load(file)
    return {}

# Function to save user data
def save_user_data(data):
    with open('user_data.json', 'w') as file:
        json.dump(data, file, indent=4)

# Function to load tasks for a user
def load_user_tasks(username):
    data = load_user_data()
    return data.get(username, {}).get('tasks', [])

# Function to save tasks for a user
def save_user_tasks(username, tasks):
    data = load_user_data()
    if username not in data:
        data[username] = {'password': data[username]['password'], 'tasks': []}
    data[username]['tasks'] = tasks
    save_user_data(data)

# Function to create a task
def create_task(username):
    while True:
        task_name = input("Enter task name (or 'back' to return to the main menu): ")
        if task_name.lower() == 'back':
            return
        due_date = input("Enter due date: ")
        priority = input("Enter priority (Low/Med/High): ")
        task = {'name': task_name, 'due_date': due_date, 'priority': priority}
        user_tasks[username].append(task)
        save_user_tasks(username, user_tasks[username])
        print(f"Task '{task_name}' created successfully!")

# Function to update a task
def update_task(username, index=None):
    if not user_tasks[username]:
        print("No tasks available to update.")
        return

    if index is None:
        view_tasks(username, update_mode=True)
        task_number = input("Enter the task number you want to update (or 'back' to return to the main menu): ")
        if task_number.lower() == 'back':
            return
        if not (task_number.isdigit() and 1 <= int(task_number) <= len(user_tasks[username])):
            print("Invalid task number.")
            return
        index = int(task_number) - 1

    task = user_tasks[username][index]

    task_name = input(f"Enter new task name (current: {task['name']}) (or 'back' to return to the main menu): ")
    if task_name.lower() == 'back':
        return
    due_date = input(f"Enter new due date (current: {task['due_date']}): ")
    priority = input(f"Enter new priority (Low/Med/High) (current: {task['priority']}): ")

    task['name'] = task_name if task_name else task['name']
    task['due_date'] = due_date if due_date else task['due_date']
    task['priority'] = priority if priority else task['priority']

    save_user_tasks(username, user_tasks[username])
    print(f"Task '{task['name']}' updated successfully!")

# Function to delete a task
def delete_task(username, index=None):
    if not user_tasks[username]:
        print("No tasks available to delete.")
        return

    if index is None:
        view_tasks(username, delete_mode=True)
        task_number = input("Enter the task number you want to delete (or 'back' to return to the main menu): ")
        if task_number.lower() == 'back':
            return
        if not (task_number.isdigit() and 1 <= int(task_number) <= len(user_tasks[username])):
            print("Invalid task number.")
            return
        index = int(task_number) - 1

    confirm_delete = input("Are you sure you want to delete? Deleting this will not be able to restore it. Type 'yes' to confirm: ").lower()
    if confirm_delete == 'yes':
        deleted_task = user_tasks[username].pop(index)
        save_user_tasks(username, user_tasks[username])
        print(f"Task '{deleted_task['name']}' deleted successfully!")
    else:
        print("Deletion canceled.")

# Function to view tasks and manage them
def view_tasks(username, update_mode=False, delete_mode=False):
    if not user_tasks[username]:
        print("No tasks available.")
        return

    for index, task in enumerate(user_tasks[username], start=1):
        print(f"Task {index}: {task['name']}")
        print(f"Due: {task['due_date']}")
        print(f"Priority: {task['priority']}")
        print("--------------------------------")

    if not update_mode and not delete_mode:
        while True:
            print("Options: [add] Create Task, [update] Update Task, [delete] Delete Task, [back] Main Menu")
            action = input("Enter your choice: ").lower()
            if action == "add":
                create_task(username)
            elif action == "update":
                task_number = input("Enter the task number to update (or 'back' to return to the main menu): ")
                if task_number.lower() == 'back':
                    break
                if task_number.isdigit() and 1 <= int(task_number) <= len(user_tasks[username]):
                    update_task(username, int(task_number) - 1)
                else:
                    print("Invalid task number.")
            elif action == "delete":
                task_number = input("Enter the task number to delete (or 'back' to return to the main menu): ")
                if task_number.lower() == 'back':
                    break
                if task_number.isdigit() and 1 <= int(task_number) <= len(user_tasks[username]):
                    delete_task(username, int(task_number) - 1)
                else:
                    print("Invalid task number.")
            elif action == "back":
                break
            else:
                print("Invalid choice. Please try again.")

# Function to search tasks by name
def search_task_by_name(username):
    while True:
        search_name = input("Enter the task name to search (or 'back' to return to the main menu): ").strip().lower()
        if search_name.lower() == 'back':
            return
        found_tasks = [task for task in user_tasks[username] if search_name in task['name'].lower()]

        if found_tasks:
            print("Found tasks:")
            for index, task in enumerate(found_tasks, start=1):
                print(f"Task {index}: {task['name']}")
                print(f"Due: {task['due_date']}")
                print(f"Priority: {task['priority']}")
                print("--------------------------------")

            while True:
                print("Options: [update] Update Task, [delete] Delete Task, [back] Main Menu")
                action = input("Enter your choice: ").lower()
                if action == "update":
                    task_number = input("Enter the task number to update (or 'back' to return to the main menu): ")
                    if task_number.lower() == 'back':
                        break
                    if task_number.isdigit() and 1 <= int(task_number) <= len(found_tasks):
                        task_index = user_tasks[username].index(found_tasks[int(task_number) - 1])
                        update_task(username, task_index)
                    else:
                        print("Invalid task number.")
                elif action == "delete":
                    task_number = input("Enter the task number to delete (or 'back' to return to the main menu): ")
                    if task_number.lower() == 'back':
                        break
                    if task_number.isdigit() and 1 <= int(task_number) <= len(found_tasks):
                        task_index = user_tasks[username].index(found_tasks[int(task_number) - 1])
                        delete_task(username, task_index)
                    else:
                        print("Invalid task number.")
                elif action == "back":
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print(f"No tasks found with the name '{search_name}'.")

# Function to display help information
def display_help():
    print(r"""
Help:
1. Create Task: Allows you to create a new task by specifying a name, due date, and priority.
2. View Tasks: Displays all tasks and provides options to add, update, and delete tasks.
3. Update Task: Allows you to update the details of an existing task.
4. Delete Task: Allows you to delete an existing task.
5. Search Task by Name: Allows you to search for a task by its name.
6. Exit: Exits the application.
Use the appropriate number or command to navigate through the system.
""")

# Function to display the main menu
def display_main_menu():
    print(r"""
                     _       _       _______        _      __  __                                              _      _____           _                 
     /\             | |     ( )     |__   __|      | |    |  \/  |                                            | |    / ____|         | |                
    /  \   _ __   __| |_   _|/ ___     | | __ _ ___| | __ | \  / | __ _ _ __   __ _  __ _ _ __ ___   ___ _ __ | |_  | (___  _   _ ___| |_ ___ _ __ ___  
   / /\ \ | '_ \ / _` | | | | / __|    | |/ _` / __| |/ / | |\/| |/ _` | '_ \ / _` |/ _` | '_ ` _ \ / _ \ '_ \| __|  \___ \| | | / __| __/ _ \ '_ ` _ \ 
  / ____ \| | | | (_| | |_| | \__ \    | | (_| \__ \   <  | |  | | (_| | | | | (_| | (_| | | | | | |  __/ | | | |_   ____) | |_| \__ \ ||  __/ | | | | |
 /_/    \_\_| |_|\__,_|\__, | |___/    |_|\__,_|___/_|\_\ |_|  |_|\__,_|_| |_|\__, |\__,_|_| |_| |_|\___|_| |_|\__| |_____/ \__, |___/\__\___|_| |_| |_|
                        __/ |                                                  __/ |                                         __/ |                      
                       |___/                                                  |___/                                         |___/                                     
""")
    print("--------------------------------")
    print("|         Task Manager         |")
    print("--------------------------------")
    print("| 1. Create Task               |")
    print("| 2. View Tasks                |")
    print("| 3. Update Task               |")
    print("| 4. Delete Task               |")
    print("| 5. Search Task by Name       |")
    print("| 6. Help                      |")
    print("| 7. Exit                      |")
    print("--------------------------------")
    print("| Please enter your choice: _  |")
    print("--------------------------------")

# Function to handle login
def login():
    print(r"""
  _                   _____       
 | |                 |_   _|      
 | |     ___   __ _    | |  _ __  
 | |    / _ \ / _` |   | | | '_ \ 
 | |___| (_) | (_| |  _| |_| | | |
 |______\___/ \__, | |_____|_| |_|
               __/ |              
              |___/               
          """)
    user_data = load_user_data()
    print("This management system takes 5 minutes to set up an account and use and another five minutes to learn! Above all, it is completely free!")
    print(
        "Welcome to Andy's task management system! This is a task management system allowing users to better manage their tasks for the day similar to having a planner. This application will allow you to create, look up, delete, and edit your tasks for ease of use.\nPlease enter your username. Otherwise, "
        "enter 'new' to create a new account ")
    username = input().strip()

    if username.lower() == 'new':
        create_account()
    elif username in user_data:
        password = input("Please enter your password: ").strip()
        if user_data[username]['password'] == password:
            print("Login successful.")
            main_menu(username)
        else:
            print("Incorrect password. Please try again.")
            login()
    else:
        print("Username not found. Please try again.")
        login()

# Function to create a new account
def create_account():
    print("\nCreate Account Page")
    user_data = load_user_data()
    username = input("Please enter your username, or enter 'back' to go back to the previous page: ").strip()
    if username.lower() == 'back' or username == '':
        login()
    password = input("Please enter your password, or enter 'back' to go back to the previous page: ").strip()
    if password.lower() == 'back' or password == '':
        login()
    confirm_password = input("Please enter your password again to confirm: ").strip()

    if password != confirm_password:
        print("Your passwords do not match. Please try again.")
        create_account()

    if username in user_data:
        print("An account with this username already exists. Please log in.")
        login()
    else:
        user_data[username] = {'password': password, 'tasks': []}
        save_user_data(user_data)
        print("Account created successfully.")
        login()

# Main menu after login
def main_menu(username):
    # Initialize user's task list if not already present
    user_tasks[username] = load_user_tasks(username)
    while True:
        display_main_menu()
        choice = input("Please enter your choice: ")

        if choice == "1":
            create_task(username)
        elif choice == "2":
            view_tasks(username)
        elif choice == "3":
            update_task(username)
        elif choice == "4":
            delete_task(username)
        elif choice == "5":
            search_task_by_name(username)
        elif choice == "6":
            display_help()
        elif choice == "7":
            print("Exiting...")
            save_user_tasks(username, user_tasks[username])
            break
        else:
            print("Invalid choice. Please try again.")

# Main application loop
if __name__ == "__main__":
    login()
