import json
import bcrypt
import msvcrt
import os

# File to store user data
USER_DATA_FILE = 'users_data.json'

# Function to load users data from JSON file 
def load_users_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Function to save users data to JSON file
def save_users_data(users_data):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users_data, file, indent=4)

# Function to handle masked password input
def masked_input(prompt="Enter your password: "):
    print(prompt, end="", flush=True)
    password = ""
    while True:
        char = msvcrt.getch()
        if char in {b"\r", b"\n"}:  # Enter key
            break
        elif char == b"\x08":  # Backspace key
            if len(password) > 0:
                password = password[:-1]
                print("\b \b", end="", flush=True)  # Remove last '*'
        else:
            password += char.decode("utf-8")
            print("*", end="", flush=True)  # Display '*'
    print()  # Move to the next line
    return password

def style_text(
    text,
    color=None,
    bg_color=None,
    bold=False,
    italic=False,
    underline=False,
    strikethrough=False,
    invert=False
):
    codes = []

    # Add text effects
    if bold:
        codes.append("1")
    if italic:
        codes.append("3")
    if underline:
        codes.append("4")
    if strikethrough:
        codes.append("9")
    if invert:
        codes.append("7")

    if color:
        codes.append(f"38;2;{color[0]};{color[1]};{color[2]}")

    if bg_color:
        codes.append(f"48;2;{bg_color[0]};{bg_color[1]};{bg_color[2]}")

    style_code = ";".join(codes)
    return f"\033[{style_code}m{text}\033[0m" if codes else text


def signup_user_id(): # get a last user id
    return users_data[len(users_data)-1]["user_id"] +1

def signup_username():
    while True:
        username = input("Enter your username: ").strip()
        if not (username.isalnum() and 3 <= len(username) <= 20):
            print("Invalid username. Must be alphanumeric and 3-20 characters long.")
            continue  
        for user in users_data:
            if user["user_name"] == username:
                print(f"Username '{username}' is already taken. Try another!")
                break  
        else:
            return username

def signup_password():
    while True:
        password = input("Enter your password: ").strip()
        if len(password) < 6:  
            print("Password too short. It must be at least 6 characters.")
            continue
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return hashed_password  

def check_password(entered_password, hashed_password):
    if bcrypt.checkpw(entered_password.encode('utf-8'), hashed_password.encode('utf-8')):
        print("Password matches.")
        return True
    else:
        print("Incorrect password.")
        return False

subjects = {
    "U": "Urdu",
    "E": "English",
    "P": "Physics",
    "C": "Chemistry",
    "M": "Mathematics"
}

def signup_subjects():
    while True:
        for initial, sbj in subjects.items():
            print(f"<{initial}> {sbj} ", end="| " if initial != list(subjects.keys())[-1] else "\n")
        
        user_input = input("Enter your subjects (comma-separated): ").upper()
        selected_subjects = [subjects[initial.strip()] for initial in user_input.split(',') if initial.strip() in subjects]

        if selected_subjects:
            print(f"You have selected: {', '.join(selected_subjects)}")
            return selected_subjects
            break
        else:
            print("Invalid selection, please choose subjects from the list.")

def students_list():
    print(
       "\b ______________________________________________________Students List______________________________________________________ \n")
    print("+ User Id +-- User Name --+---- Name -----+-- Last Name --+- Role --+-- Age --+---------------- Subjects ---------------+")
    for user in users_data:
        if user["role"] == "s":
            data = "|"
            space = ""
            for k in user.keys():
                if k != "password" and k != "students": 
                    space = ""
                    col_size = 14
                    if k == "subjects" or k == "students":
                        col_size = 40
                    elif k == "user_id" or k == "role" or k == "age":
                        col_size = 8

                    for s in range(col_size-len(str(user[k]))):
                        space = " " * s
                    data += f" {user[k]}{space} |"
            print(data)
            print("+---------+---------------+---------------+---------------+---------+---------+-----------------------------------------+")
            
def signup_students():
    students_list()            
    user_input = input("Enter your students (comma-separated): ")
    selected_students = user_input.split(",")
    print(selected_students)
    students = []
    for input_id in selected_students:
        for user in users_data:
            if user["user_id"] == int(input_id):
                students.append(user["name"])
    return students
        
def signup_role():
    while True:
        role = input("Enter your role (t or s): ").lower()  
        if role == 't' or role == 's':
            return role
            break
        else:
            print("Invalid role! Please enter 't' or 's'.")

def signup_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                print("Please enter a positive age.")
            else:
                return age
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer for your age.")


def navigation(username, enter_by):
    action = input("Enter your action: ").lower()
    if action == 'a':
        students_list()
    elif action == 'e':
        examinations(username)
        pass
    elif action == 'n':
        login_signup('s')
    elif action == 'l':
        main()
    elif action == 'b':
        login_signup(enter_by)

def date_formate(date_formate):
    split_date = date_formate.split("/")

    if not split_date[3:] and split_date[0].isdigit() and split_date[1].isdigit() and split_date[2].isdigit():
        if int(split_date[0]) <= 31 and int(split_date[0]) > 0 and int(split_date[1]) <= 12 and int(split_date[1]) > 0 and int(split_date[2]) > 1971:
            return True
        else:
            return False
    else:
        return False
    
def time_formate(time_formate):
    split_time = time_formate.split(":")

    if not split_time[3:] and split_time[0].isdigit() and split_time[1].isdigit() and split_time[2].isdigit():
        if int(split_time[0]) <= 24 and int(split_time[0]) > 0 and int(split_time[1]) <= 60 and int(split_time[1]) > 0 and int(split_time[2]) > 60:
            return True
        else:
            return False
    else:
        return False
    
def examinations(username):
    while True:
        date = input("Enter date as DD/MM/YY: ")
        if date_formate(date):
            time = input("Enter time as '00:00:00': ")
            if time_formate(date):
                place = input("Enter place addras: ")
                for user in users_data:
                    if user['user_name'] == username:
                        user['date'] = date,
                        user['time'] = time,
                        user['place'] = place,
            else:
                print("Invalid time! Please enter a valid time as hr/min/sec")
        else:
            print("Invalid date! Please enter a valid date as Date/Month/Year")

def student_dashboard(username, enter_by, mode):
    is_user = False
    for user in users_data:
        if user['user_name'] == username: 
            num = []
            is_user = True
            if mode == 'c':
                num = [["", False], ["", False], ["", False], ["", False], ["",False], ["",False], ["1.",False], ["2.",False],     ["3.",False], ["4.",False]]
            elif mode == 'r':
                num = [["", False], ["", False], ["", False], ["", False], ["",False], ["",False], ["",False], ["",False], ["",False], ["",False]]
            elif mode == 'u':
                num = [["0.", False], ["1.", False], ["2.", False], ["3.", False], ["4.", False], ["5",False], ["6.",False], ["7.",False], ["8.",False], ["9.",False], ["10.",False]]
            else:    
                num = [["", False], ["", False], ["1.", False], ["", False], ["2.",False], ["",False], ["3.",False], ["4.",False], ["",False], ["",False]]

            # Print the user dashboard
            print(f'''
            \n\t\t \t  ------ Student Dashboard ({num[0][0]+user["user_name"]}) ------ \n
               -- MENUE --  |        Creat    |    Read    |    Update    |    Delete \n
                                INFO
            <E> Examinations|   \t{style_text(num[1][0]+"Name: "+user["name"], underline=False)} \t\t{style_text(num[2][0]+"Last Name: "+user["last_name"], underline=num[2][1])}
            <N> New acount  |   \t{style_text(num[3][0]+"Role: "+user["role"], underline=num[3][1])} \t{style_text(f"{num[4][0]}Age: {user["age"]}", underline=num[4][1])} \t{style_text(num[5][0]+"Teacher Name: N/A", underline=num[5][1])}
            <L> Logout      |     _______________________________________________________________________
            <B> Back        |   CORSE
           <P> PrivitPolices|   \t{num[6][0]}Subjects: 
                            |   \t\t{style_text(', '.join(user.get("subjects", [])), underline=num[6][1])}
                            |   \t{num[7][0]}Exams:
                            |   \t\t{style_text(f"Date: {user["date"]}\tTime: {user["time"]}\t\tPlace: {user["place"]}", underline=num[7][1])}
            
            ''')
            navigation(username, enter_by)
        else:
            is_user 
            
    if not is_user:
        print(f"User {username} not found!")

def teacher_dashboard(username, enter_by, mode):
    is_user = False
    for user in users_data:
        if user['user_name'] == username: 
            num = []
                
            is_user = True
            if mode == 'c':
                num = [["", False], ["", False], ["", False], ["", False], ["",False], ["",False], ["1.",True], ["2.",True],     ["3.",True], ["4.",True]]
            elif mode == 'r':
                num = [["", False], ["", False], ["", False], ["", False], ["",False], ["",False], ["",False], ["",False], ["",False], ["",False]]
            elif mode == 'u':
                num = [["0.", True], ["1.", True], ["2.", True], ["3.", True], ["4.", True], ["5",True], ["6.",True], ["7.",True], ["8.",True], ["9.",True], ["10.",True]]
            else:    
                num = [["", False], ["", False], ["1.", True], ["", False], ["2.",True], ["",False], ["3.",True], ["4.",True], ["",False], ["",False]]

            # Print the user dashboard
            print(f'''
            \n\t\t \t  ------ Teacher Dashboard ({num[0][0]+user["user_name"]}) ------ \n
               -- MENUE --  |        Creat    |    Read    |    Update    |    Delete \n
                                INFO
            <A> All Students|   \t{style_text(num[1][0]+"Name: "+user["name"], underline=False)} \t\t{style_text(num[2][0]+"Last Name: "+user["last_name"], underline=num[2][1])}
            <N> New acount  |   \t{style_text(num[3][0]+"Role: "+user["role"], underline=num[3][1])} \t{style_text(f"{num[4][0]}Age: {user["age"]}", underline=num[4][1])} 
            <L> Logout      |     _______________________________________________________________________
            <B> Back        |   CLASS
           <P> PrivitPolices|   \t{num[6][0]}Students: 
                            |   \t\t{style_text(', '.join(user.get("students", [])), underline=num[6][1])}           
            ''')
            navigation(enter_by)
        else:
            is_user 
            
    if not is_user:
        print(f"User {username} not found!")



# Main program 
stage = "home page"
users_data = load_users_data()  # Load existing user data

def login_signup(action):
    if action == 's':
        print("\n\t------ Signup here, <T> Teacher | <S> Student ------\n")
        user_id = signup_user_id()
        user_name = signup_username()
        password = signup_password()
        role = signup_role()
        name = input("Enter your name: ")
        last_name = input("Enter your last name: ")
        age = signup_age()
        subjects = students = []
        teacher = ""
        if role == 't':
            students = signup_students()
            teacher = False
        else:
            subjects = signup_subjects()
            teacher = "No Teacher!"
        users_data.append({
            "user_id": user_id,
            "user_name": user_name,
            "password": password,
            "name": name,
            "last_name": last_name,
            "role": role,
            "age": age,
            "subjects": subjects,
            "students": students,
            "teacher": teacher,
        })
        save_users_data(users_data)
        print(f"Signup successful! Welcome, {name}.")
        if role == 't':
            teacher_dashboard(user_name, action, 'r')
        else:
            student_dashboard(user_name, action, 'r')
    else:
        print("\n\t------ Login here, <T> Teacher | <S> Student ------\n")
        while True:
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            login_successful = False

            for user in users_data:
                if user['user_name'] == username: 
                    if check_password(password, user['password']):
                        print(f"Login successful! Welcome, {username}.")
                        if user['role'] == 't':
                            teacher_dashboard(username, action, 'r')
                        else:
                            student_dashboard(username, action, 'r') 
                        login_successful = True
                        break  
                    else:
                        print("Invalid username or password. Please try again.\n")
                        login_successful = True  
                        break  
                    
            if not login_successful:
                print("Invalid username or password. Please try again.\n")
    
user_name = ""

# Main program
def main():
    print("\n\t------ Welcome to the, Student Management System! ------\n")
    action = input("Choose an action:\n\t<L> Login  <S> Signup  <E> Exit\n").lower()
    if action in {"l", "s"}:
        login_signup(action)
    else:
        print(f"\t\t\t*** Exiting the program. Goodbye, {users_data[user_name]['name']}! ***")
        
# Calling Main program
while True:
    main()  

