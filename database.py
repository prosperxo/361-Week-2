import json
import os

# Dictionary to store images for each user
user_images = {}

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

# Function to load images for a user
def load_user_images(username):
    data = load_user_data()
    return data.get(username, {}).get('images', [])

# Function to save images for a user
def save_user_images(username, images):
    data = load_user_data()
    if username not in data:
        data[username] = {'password': data[username]['password'], 'images': []}
    data[username]['images'] = images
    save_user_data(data)

# Function to upload an image
def upload_image(username):
    while True:
        image_path = input("Enter image file location (or 'back' to return to the main menu): ")
        if image_path.lower() == 'back':
            return
        if os.path.exists(image_path):
            user_images[username].append(image_path)
            save_user_images(username, user_images[username])
            print(f"Image '{image_path}' uploaded successfully!")
        else:
            print("Invalid file location. Please try again.")

# Function to delete an image
def delete_image(username):
    user_images[username] = load_user_images(username)
    if not user_images[username]:
        print("No images available.")
        return

    for index, image in enumerate(user_images[username], start=1):
        print(f"Image {index}: {image}")
        print("--------------------------------")

    while True:
        image_number = input("Enter the image number you want to delete (or 'back' to return to the main menu): ")
        if image_number.lower() == 'back':
            return
        if image_number.isdigit() and 1 <= int(image_number) <= len(user_images[username]):
            image_number = int(image_number) - 1
            confirm = input(f"Are you sure you want to delete '{user_images[username][image_number]}'? Type 'yes' to confirm: ")
            if confirm.lower() == 'yes':
                deleted_image = user_images[username].pop(image_number)
                save_user_images(username, user_images[username])
                print(f"Image '{deleted_image}' deleted successfully!")
            else:
                print("Deletion cancelled.")
            return
        else:
            print("Invalid image number. Please try again.")

# Function to view uploaded images
def view_images(username):
    user_images[username] = load_user_images(username)
    if not user_images[username]:
        print("No images available.")
        return

    for index, image in enumerate(user_images[username], start=1):
        print(f"Image {index}: {image}")
        print("--------------------------------")

    while True:
        action = input("Options: [delete] Delete Image, [back] Main Menu: ").lower()
        if action == 'delete':
            delete_image(username)
        elif action == 'back':
            return
        else:
            print("Invalid choice. Please try again.")

# Function to display help information
def display_help():
    print(r"""
Help:
1. Upload Image: Allows you to upload an image by specifying its file location.
2. View Images: Displays all uploaded images and provides an option to delete them.
3. Delete Image: Allows you to delete an uploaded image.
4. Exit: Exits the application.
Use the appropriate number or command to navigate through the system.
""")

# Function to display the main menu
def display_main_menu():
    print(r"""
  _____  _           _          _____        _        _                    
 |  __ \| |         | |        |  __ \      | |      | |                   
 | |__) | |__   ___ | |_ ___   | |  | | __ _| |_ __ _| |__   __ _ ___  ___ 
 |  ___/| '_ \ / _ \| __/ _ \  | |  | |/ _` | __/ _` | '_ \ / _` / __|/ _ \
 | |    | | | | (_) | || (_) | | |__| | (_| | || (_| | |_) | (_| \__ \  __/
 |_|    |_| |_|\___/ \__\___/  |_____/ \__,_|\__\__,_|_.__/ \__,_|___/\___|
                                                                           
                                                                                                            
""")
    print("--------------------------------")
    print("|         Image Manager        |")
    print("|------------------------------|")
    print("| 1. Upload Image              |")
    print("| 2. View Images               |")
    print("| 3. Delete Image              |")
    print("| 4. Help                      |")
    print("| 5. Exit                      |")
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
    print("This management system takes five minutes to set up an account and use and another five minutes to learn! Above all, it is completely free!")
    print(
        "Welcome to the image management system! This application will allow you to upload and view images easily.\nPlease enter your username. Otherwise, "
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
        user_data[username] = {'password': password, 'images': []}
        save_user_data(user_data)
        print("Account created successfully.")
        login()

# Main menu after login
def main_menu(username):
    # Initialize user's image list if not already present
    user_images[username] = load_user_images(username)
    while True:
        display_main_menu()
        choice = input("Please enter your choice: ")

        if choice == "1":
            upload_image(username)
        elif choice == "2":
            view_images(username)
        elif choice == "3":
            delete_image(username)
        elif choice == "4":
            display_help()
        elif choice == "5":
            print("Exiting...")
            save_user_images(username, user_images[username])
            break
        else:
            print("Invalid choice. Please try again.")

# Main application loop
if __name__ == "__main__":
    login()
