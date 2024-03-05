import os
import json
import re
from datetime import datetime

def add_data(data, pathFile):
        with open(pathFile, "w") as file:
            json.dump(data, file, indent=4)

def get_data(pathFile):
        if os.path.exists(pathFile):
            with open(pathFile, "r") as file:
                return json.load(file)
        else:
            return []

def login(pathFile):
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    users = get_data(pathFile)
    for user in users:
        if user["email"] == email and user["password"] == password:
            print("login successful!")
            userOperation(email ,pathFile)
    print("Invalid email or password. Please try again.")

def register(path_file):
    print("Register for a new account:")
    firstname = input("First name: ")
    lastname = input("Last name: ")
    email = input("Email: ")
    password = input("Password: ")
    repassword = input("Re-enter Password: ")

    if password != repassword:
        print("Passwords do not match. Please try again.")
        return register(path_file)
    
    phone = input("Mobile phone (Egyptian number starting with 01): ")

    if not validate_email(email):
        print("Invalid email format. Please enter a valid email.")
        return register(path_file)

    if not validate_phone(phone):
        print("Invalid phone number format. Please enter a valid Egyptian phone number.")
        return register(path_file)

    existing_data = get_data(path_file)

    if not existing_data:
        existing_data = []

    user_data = {"firstname": firstname, "lastname": lastname, "email": email, "password": password, "phone": phone, "projects": []}
    existing_data.append(user_data)
    print(user_data)
    add_data(existing_data, path_file)

    print("User registered successfully!")

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

def validate_phone(phone):
    phone_regex = r'^01[0-9]{9}$'
    return re.match(phone_regex, phone)

def userOperation(email,pathFile):
    while True:
        print("\nMenu:")
        print("1. View all projects")
        print("2. Add project")
        print("3. Edit your projects")
        print("4. Delete your projects")
        print("5. Search for a project")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all_projects(email,pathFile)
        elif choice == "2":
            add_projects(email,pathFile)
        elif choice == "3":
            edit_projects(email,pathFile)
        elif choice == "4":
            delete_projects(email,pathFile)
        elif choice == "5":
            search_project(email,pathFile)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def view_all_projects(email ,pathFile):
    projects_data = get_data(pathFile)
    print("Viewing all projects...")

def authentication(email, path_file):
    exist_users = get_data(path_file)
    count=0
    for user in exist_users:
        if user["email"] == email:

            return {"auth":True ,"index":count}
        count+=1
        return {"auth":False ,"index":count}
   

def add_projects(email, path_file):

    is_Auth = authentication(email, path_file)
    if is_Auth["auth"]:
        data = get_data(path_file)

    title = input("Enter project title: ")
    while not title.strip():  
        print("Project title cannot be empty.")
        title = input("Enter project title: ")

    details = input("Enter project details: ")
    while not details.strip():
        print("Project details cannot be empty.")
        details = input("Enter project details: ")

    total_target = input("Enter total target amount: ")
    while not total_target.strip():
        print("Total target amount cannot be empty.")
        total_target = input("Enter total target amount: ")


        while True:
            start_time_str = input("Enter project start time (YYYY-MM-DD HH:MM): ")
            try:
                start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
                break
            except ValueError:
                print("Invalid date format. Please enter in YYYY-MM-DD HH:MM format.")

        while True:
            end_time_str = input("Enter project end time (YYYY-MM-DD HH:MM): ")
            try:
                end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
                if end_time <= start_time:
                    print("End time must be after start time. Please enter a valid end time.")
                    continue
                break
            except ValueError:
                print("Invalid date format. Please enter in YYYY-MM-DD HH:MM format.")

   
        project_data = {
            "title": title,
            "details": details,
            "total_target": total_target,
            "start_time": start_time.strftime("%Y-%m-%d %H:%M"),
            "end_time": end_time.strftime("%Y-%m-%d %H:%M")
        }

        data[is_Auth["index"]]["projects"].append(project_data)

        add_data(data, path_file)

        print("Project added successfully!")
    else:
        print("Authentication failed. Please login.")
        login(path_file)


def edit_projects(email, path_file):
    is_Auth = authentication(email, path_file)
    if is_Auth["auth"]:
        data = get_data(path_file)

        if not data[is_Auth["index"]]["projects"]:
            print("You have no projects to edit.")
            return

        print("Editing your projects...")
        
        print("Your Projects:")
        projects = data[is_Auth["index"]]["projects"]
        for i, project in enumerate(projects):
            print(f"{i+1}. {project['title']}")
        
        try:
            project_index = int(input("Enter the number of the project you want to update: ")) - 1
            if project_index < 0 or project_index >= len(projects):
                print("Invalid project number.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid project number.")
            return


        project = projects[project_index]
        print(f"Updating project '{project['title']}':")
        project["title"] = input("Enter updated project title: ")
        project["details"] = input("Enter updated project details: ")
        project["total_target"] = input("Enter updated total target amount: ")
        while True:
            start_time_str = input("Enter updated project start time (YYYY-MM-DD HH:MM): ")
            try:
                start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
                break
            except ValueError:
                print("Invalid date format. Please enter in YYYY-MM-DD HH:MM format.")
        while True:
            end_time_str = input("Enter updated project end time (YYYY-MM-DD HH:MM): ")
            try:
                end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
                if end_time <= start_time:
                    print("End time must be after start time. Please enter a valid end time.")
                    continue
                break
            except ValueError:
                print("Invalid date format. Please enter in YYYY-MM-DD HH:MM format.")
        project["start_time"] = start_time.strftime("%Y-%m-%d %H:%M")
        project["end_time"] = end_time.strftime("%Y-%m-%d %H:%M")


        add_data(data, path_file)

        print("Project updated successfully!")
    else:
        print("Authentication failed. Please login.")
        login(path_file)

def delete_projects(email, path_file):
    is_Auth = authentication(email, path_file)
    if is_Auth["auth"]:
        data = get_data(path_file)

        if not data[is_Auth["index"]]["projects"]:
            print("You have no projects to delete.")
            return

        print("Deleting your projects...")
        
        print("Your Projects:")
        projects = data[is_Auth["index"]]["projects"]
        for i, project in enumerate(projects):
            print(f"{i+1}. {project['title']}")

        try:
            project_index = int(input("Enter the number of the project you want to delete: ")) - 1
            if project_index < 0 or project_index >= len(projects):
                print("Invalid project number.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid project number.")
            return


        confirm = input("Are you sure you want to delete this project? (yes/no): ").lower()
        if confirm != "yes":
            print("Deletion cancelled.")
            return

        del projects[project_index]

        add_data(data, path_file)

        print("Project deleted successfully!")
    else:
        print("Authentication failed. Please login.")
        login(path_file)

def search_project(email, path_file):
    is_Auth = authentication(email, path_file)
    if is_Auth["auth"]:
        data = get_data(path_file)

        if not data[is_Auth["index"]]["projects"]:
            print("You have no projects to search.")
            return

        print("Searching for a project...")

        search_date_str = input("Enter the date to search for projects (YYYY-MM-DD): ")
        try:
            search_date = datetime.strptime(search_date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter in YYYY-MM-DD format.")
            return

        found_projects = []
        for project in data[is_Auth["index"]]["projects"]:
            start_time = datetime.strptime(project["start_time"], "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(project["end_time"], "%Y-%m-%d %H:%M")
            if start_time.date() <= search_date.date() <= end_time.date():
                found_projects.append(project)

        if found_projects:
            print("Found projects:")
            for i, project in enumerate(found_projects):
                print(f"{i+1}. {project['title']}")
        else:
            print("No projects found for the specified date.")
    else:
        print("Authentication failed. Please login.")
        login(path_file)


file_path = "user_data.json"  
    
while True:
    print("Hello, do you have an account?")
    choice = input("Enter 'yes' or 'no': ").lower()

    if choice == "yes":
        login(file_path)
    elif choice == "no":
        register(file_path)
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

