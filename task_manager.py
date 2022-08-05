# The program below helps to manage tasks assigned to each member of a team in a small business

from datetime import date

# Files
user_txt = 'user.txt'
task_txt = 'tasks.txt'

# Login Section
while True:

    # Requesting user for credentials
    username = input("Please provide your valid username: \n")
    password = input(f"{username}, Please provide your valid password: \n")

    credentials = f"{username}, {password}"

    with open(user_txt, 'r') as credentials_file:
        credentials_validation = credentials_file.read()

        # Validating user credentials to log in.
        if credentials in credentials_validation:
            print(f"\n{username}, you are successfully logged in")
            break

        # Results shown when user enters a username that is not listed i the user.txt
        if username not in credentials_validation:
            print("\nIncorrect username, please try again")
            continue

        # Results shown when a user enters a valid username but not a valid password.
        if username in credentials_validation and password not in credentials_validation:
            print("\nIncorrect Password, please try again")
            continue

# Main program
while True:

    # Presenting the menu to the user and making sure that the user input is converted to lower case.
    menu = input('''\nSelect one of the following Options below:
r - Registering a user 'only admin'
a - Adding a task
va - View all tasks
vm - view my task
st - statistics for admin
e - Exit
: ''').lower()

    # Registering a new user
    if menu == 'r':

        if username == 'admin':

            # Requesting user for inputs
            new_username = input("Please provide a username: \n")
            password = input("Please provide a password: \n")
            password_confirmation = input(f"Please {new_username}, confirm your password. \n")

            # Opening the txt file to add information
            if password == password_confirmation:
                with open(user_txt, 'a') as user_file:
                    valid_info = f"{new_username.lower()}, {password}"

                    # Writing the user information to the file
                    user_file.write(f"{valid_info}\n")
                    print(f"\n{new_username}, is successfully registered.")

            else:
                print(f"{new_username},your password is not matching your confirmed password, \n restart and try again")
                continue

        if username != 'admin':
            print("Only the admin is allowed to register new users.")

    # Adding a task for a user, this option can only be performed by the admin.
    elif menu == 'a':

        with open(user_txt, 'r') as logged_admin:
            contents = logged_admin.readlines()

            # Requesting user for inputs
            user = input("Please a provide username for the person to be tasked: \n")
            title_of_task = input(f"Please enter the title task for {user}:  \n")
            description_of_task = input(f"Now enter a description for the task: \n")
            due_date = input("Please provide the due date for the task in this format (DD MM YY): \n")

            task_completed = "No"

            # Obtaining the current date the task was added
            current_date = date.today()
            final_current_date = current_date.strftime("%d %m %Y")

            # Opening the txt file to add information
            with open(task_txt, 'a') as task_file:
                tasks = f"{user}, {title_of_task}, {description_of_task}, " \
                        f"{final_current_date}, {due_date}, {task_completed}"

                # Writing the user information to the file
                task_file.write(f"\n{tasks}")

    # Viewing all tasks of each member
    elif menu == 'va':

        with open(task_txt, 'r') as file_task:
            contents = file_task.readlines()

            space_removed = []
            for each_line in contents:

                # Removing any white space in the file IF there is.
                if each_line.strip():
                    space_removed.append(each_line)

                    # Looping through the list to access each element
                    for line in space_removed:
                        # Using indexes to obtain each task for the users and its details.
                        task = line.split(',')[1]
                        assigned_to = line.split(',')[0]
                        date_assigned = line.split(',')[3]
                        due_date = line.split(',')[4]
                        task_completed = line.split(',')[5]
                        task_description = line.split(',')[2]

                        # Printing out the results in a formatted output
                        print(f"Task:                   {task}\n"
                              f"Assigned to:             {assigned_to}\n"
                              f"Date assigned:          {date_assigned}\n"
                              f"Due date:               {due_date}\n"
                              f"Task Completed?         {task_completed}"
                              f"Task Description:       {task_description}\n"
                              )

    # Viewing all tasks of the current logged-in user
    elif menu == 'vm':

        with open('tasks.txt', 'r') as view_my_tasks:
            contents = view_my_tasks.readlines()

        # List that will hold tasks for the current logged-in user
        user_tasks = []

        for line in contents:

            if username in line:
                # Obtaining the tasks of the current logged-in user
                each_task = line.split(',')[2].strip()
                user_tasks.append(each_task)

        print(f"Assigned to : {username}")
        for tasks in user_tasks:
            print(f"Task Description : {tasks}")

    # Viewing statistics
    elif menu == 'st':

        with open(user_txt, 'r') as logged_admin:
            contents = logged_admin.readlines()

            #  Finding the total number of users
            total_num_of_users = len(contents)

        with open(task_txt, 'r') as admin_logged:
            content = admin_logged.readlines()

            space_removed = []
            for line in content:
                # Removing any white space in the file IF there is.
                if line.strip():
                    space_removed.append(line)

            #  Finding the total number of tasks
            total_num_of_tasks = len(space_removed)

        # Checking if the current logged-in user is the admin
        if username == 'admin':
            results = f"The total number of tasks is {total_num_of_tasks}\n" \
                      f"The total number of users is {total_num_of_users}"
            print("\n   \t___Statistics___")

            # Printing out the results
            print(f"{results}")

        else:
            print(f"\nOnly admin can use the 'Statistics' option.")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
