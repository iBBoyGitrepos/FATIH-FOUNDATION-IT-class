import json
import bcrypt
import msvcrt
import os
import re
from datetime import datetime
from style_text import st

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

def signup_user_id(): # get a last user id
    return users_data[len(users_data)-1]["user_id"] +1

def signup_username():
    while True:
        username = input("Enter your username: ").strip()
        if not (username.isalnum() and 3 <= len(username) <= 13):
            print("Invalid username. Must be alphanumeric and 3-13characters long.")
            continue  
        for user in users_data:
            if user["user_name"] == username:
                print(f"Username '{username}' is already taken. Try another!")
                break  
        else:
            return username

def signup_password():
    while True:
        password = masked_input("Enter your password: ")
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

def show_subjects():
    for initial, sbj in subjects.items():
        print(f"<{initial}> {sbj} ", end="| " if initial != list(subjects.keys())[-1] else "\n")
            
def signup_subjects():
    while True:
        show_subjects()
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
    st("____________________________________________________(  Students List  )___________________________________________________\n", color=(3, 173, 30)), st('''
+ User Id +-- User Name --+---- Name -----+-- Last Name --+- Role --+-- Age --+---------------- Subjects ---------------+- Teacher -+''', color=(170, 28, 20)))
    for user in users_data:
        if user["role"] == "s":
            data = st("|", color=(170, 28, 20))
            space = ""
            for k in user.keys():
                if k != "password" and k != "students": 
                    space = ""
                    col_size = 14
                    if k == "subjects" or k == "students":
                        col_size = 40
                    elif k == "user_id" or k == "role" or k == "age":
                        col_size = 8
                    elif k == "teacher":
                        col_size = 10
                        
                    for s in range(col_size-len(str(user[k]))):
                        space = " " * s
                    if not k == "exam":
                        data += f" {user[k]}{space} " + st("|", color=(170, 28, 20))
            print(data)
            print(st("+---------+---------------+---------------+---------------+---------+---------+-----------------------------------------+-----------+", color=(170, 28, 20)))
            
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

def creat(username, enter_by):
    action = input("Enter feeld number, For creat: ")
    for user in users_data:
        if user['user_name'] == username:
            if action == '1': 
                user['subjects'] = signup_subjects()
            elif action == '2':
                user['exam'] =  examinations(username, enter_by)
    save_users_data(users_data)
    student_dashboard(username, enter_by, 'r')
       
def update(username, enter_by):
    action = input("Enter field number, For update: ")
    for user in users_data:
        if user['user_name'] == username:
            if action == '1':
                user_name = signup_username()  
                user['user_name'] = user_name 
            elif action == '2':
                user['first_name'] = input("Enter your name: ")  
            elif action == '3':
                user['last_name'] = input("Enter your last name: ")
            elif action == '4':
                user['age'] = signup_age()  
            elif action == '5':
                if user['role'] == 't':
                    user['students'] = signup_students()  
                else:
                    user['subjects'] = signup_subjects(username, enter_by)  
            elif action == '6':
                user['exam'] = examinations(username, enter_by) 
            print("User data updated successfully.")
            break  
    else:
        print("User not found.")

    save_users_data(users_data)
    student_dashboard(user_name if 'user_name' in locals() else username, enter_by, 'r')
    
def delete(username, enter_by):
    action = input("Enter feeld number, For delete: ")
    for user in users_data:
        if user['user_name'] == username:
            if action == '1': 
                user['last_name'] = ""
            elif action == '2':
                user['subjects'] = []
            elif action == '3':
                user['exam'] = {
                        "subject": "None",
                        "timestamp_value": None,
                        "venue": "None"
                    }
    save_users_data(users_data)
    student_dashboard(username, enter_by, 'r')
        
def navigation(username, enter_by, action):
    if action == 'a':
        students_list()
    elif action == 'e':
        examinations(username, enter_by)
    elif action == 'n':
        login_signup('s')
    elif action == 'l':
        main()
    elif action == 'b':
        login_signup(enter_by)
    elif action == 'c':
        student_dashboard(username, enter_by, 'c')
    elif action == 'r':
        student_dashboard(username, enter_by, 'r')
    elif action == 'u':
        student_dashboard(username, enter_by, 'u')
    elif action == 'd':
        student_dashboard(username, enter_by, 'd')
    else:
        print("Invaled input, corect it!")

def date_format(date_format):
    user_date = re.findall("^(3[01]|[12][0-9]|[1-9])/(1[0-2]|[1-9])/(197[1-9]+|19[8-9][0-9]+|[2-9][0-9]{2}[0-9]+)$", date_format)
    if user_date:
        return True
    else:
        return False
    
def time_format(time_format):
    split_time = time_format.split(":")
    if len(split_time) == 3 and split_time[0].isdigit() and split_time[1].isdigit() and split_time[2].isdigit():
        hour = int(split_time[0])
        minute = int(split_time[1])
        second = int(split_time[2])

        if 0 <= hour < 24 and 0 <= minute < 60 and 0 <= second < 60:
            return True
    return False

def fromtimestamp(timestamp):
    if not timestamp == None:
        date_time = datetime.fromtimestamp(timestamp)
        date = date_time.date()  
        time = date_time.time()
    else:
        date = "None"
        time = "None"
    return [date, time]
    
def examinations(username, enter_by):
    while True:
        show_subjects()  
        subject_initial = input("Enter the subject initial (e.g., U for Urdu): ").upper()
        
        if subject_initial in subjects:
            subject = subjects[subject_initial]  
            date = input("Enter date as DD/MM/YYYY: ")
            if date_format(date):
                time = input("Enter time as 'HH:MM:SS': ")
                if time_format(time):
                    
                    # Combine date and time into a single string and convert it to a timestamp
                    datetime_str = f"{date} {time}"
                    datetime_obj = datetime.strptime(datetime_str, "%d/%m/%Y %H:%M:%S")
                    timestamp_value = datetime_obj.timestamp()
                    
                    venue = input("Enter exam hall or institute address: ")
                    for user in users_data:
                        if user['user_name'] == username:
                            user['exam'] = {"subject": subject, "timestamp_value": timestamp_value, "venue": venue}
                            save_users_data(users_data)
                    break  
                else:
                    print("Invalid time! Please enter a valid time as hr:min:sec.")
            else:
                print("Invalid date! Please enter a valid date as DD/MM/YYYY.")
        else:
            print("Invalid subject! Please select a valid subject.")
    student_dashboard(username, enter_by, 'r')

def crud_mode(mode):
    if mode == 'c':
        num = [["", False], ["", False], ["", False], ["", False], ["1 ",False], ["2 ",False], ["", False]]
    elif mode == 'r':
        num = [["", False], ["", False], ["", False], ["", False], ["",False], ["",False], ["",False]]
    elif mode == 'u':
        num = [["1 ", False], ["2 ", False], ["3 ", False], ["4 ", False], ["5 ", False], ["6 ",False]]
    else:    
        num = [["", False], ["", False], ["1 ", False], ["", False], ["2 ",False], ["3 ",False]]
    return num
            
def student_dashboard(username, enter_by, mode):
    is_user = False
    for user in users_data:
        if user['user_name'] == username: 
            is_user = True
            num = crud_mode(mode)
            datetime = fromtimestamp(user["exam"]["timestamp_value"])

            # Print the student dashboard
            print(f'''
{st(f'''____________________________________________
                     \t\t\t  /
                     \t\t\t /______ Student Dashboard ({num[0][0]+user["user_name"]}) _________ 
                     \t\t\t  ------ Welcome! ({user["user_name"]}) ------ ''', color=(25, 103, 210), bold=True)}
{st('''
               -- MENUE --  |        Creat    |    Read    |    Update    |    Delete                                            ''', 
bg_color=(0, 255, 0), color=(237, 42, 31), bold=True)} \n
                                {st("INFO", color=(1, 18, 48))}
             {st("<E>",color=(237, 42, 31))}Examinations|   \t{st(num[1][0]+"Name: "+user["name"], underline=False)} \t\t{st(num[2][0]+"Last Name: "+user["last_name"], underline=num[2][1])}
             {st("<N>",color=(237, 42, 31))}New acount  |   \t{st("Role: "+user["role"])} \t{st(f"{num[3][0]}Age: {user["age"]}", underline=num[3][1])} \t{st("Teacher Name: N/A")}
             {st("<L>",color=(237, 42, 31))}Logout      |     _______________________________________________________________________
             {st("<B>",color=(237, 42, 31))}Back        |   {st("CORSE", color=(1, 18, 48))}
             {st("<P>",color=(237, 42, 31))}PrivitPolice|   \t{num[4][0]}Subjects: 
                            |   \t\t{st(', '.join(user.get("subjects", [])), underline=num[4][1])} 
                            |   \t{num[5][0]}Exams:
                            |   \t\t{st(f"Subject: {user["exam"]["subject"]}\tDate: {datetime[0]}\tTime: {datetime[1]}\tVenue: {user["exam"]["venue"]}", underline=num[5][1])}
            ''') 
            action = input("Enter action: ")
            if mode == action:
                if action == 'c':
                    creat(username, enter_by)
                elif action == 'r':
                    student_dashboard(username, enter_by, 'r')
                elif action == 'u':
                    update(username, enter_by)
                elif action == 'd':
                    delete(username, enter_by)
            else:
                navigation(username, enter_by, action)
            
    if not is_user: 
        print(f"User {username} not found!")

def teacher_dashboard(username, enter_by, mode):
    is_user = False
    for user in users_data:
        if user['user_name'] == username: 
            is_user = True
            num = crud_mode(mode)

            # Print the Teacher dashboard
            print(f'''
            \n\t\t \t  ------ Teacher Dashboard ({num[0][0]+user["user_name"]}) ------ \n
               -- MENUE --  |        Creat    |    Read    |    Update    |    Delete \n
                                INFO
            <A> All Students|   \t{st(num[1][0]+"Name: "+user["name"], underline=False)} \t\t{st(num[2][0]+"Last Name: "+user["last_name"], underline=num[2][1])}
            <N> New acount  |   \t{st("Role: "+user["role"])} \t{st(f"{num[3][0]}Age: {user["age"]}", underline=num[3][1])} 
            <L> Logout      |     _______________________________________________________________________
            <B> Back        |   CLASS
            <P> PrivitPolice|   \t{num[4][0]}Students: 
                            |   \t\t{st(', '.join(user.get("students", [])), underline=num[4][1])} 
            ''') 
            action = input("Enter action: ")
            if mode == action:
                if action == 'c':
                    creat(username, enter_by)
                elif action == 'r':
                    student_dashboard(username, enter_by, 'r')
                elif action == 'u':
                    update(username, enter_by)
                elif action == 'd':
                    delete(username, enter_by)
            else:
                navigation(username, enter_by, action)
        else:
            is_user 
            
    if not is_user:
        print(f"User {username} not found!")

def login_signup(action):
    if action == 's':
        print("\n\t------ Signup here, <T> Teacher | <S> Student ------\n")
        role = signup_role()
        user_name = signup_username()
        users_data.append({ 
            "user_id": signup_user_id(),
            "user_name": user_name,
            "password": signup_password(),
            "name": input("Enter your name: "),
            "last_name": input("Enter your last name: "),
            "role": role,
            "age": signup_age(),
            "subjects": signup_subjects() if role == 's' else [],
            "students": signup_students() if role == 't' else [],
            "teacher": "Teacher" if role == 't' else "No Teacher",
            "exam": {
                "subject": "None",
                "timestamp_value": None,
                "venue": "None"
            },
        })
        print(f"Signup successful! Welcome, {user_name}.")
        save_users_data(users_data)
        if role == 't':
            teacher_dashboard(user_name, action, 'r')
        else:
            student_dashboard(user_name, action, 'r')
    elif action == 'l':
        print("\n\t------ Login here, <T> Teacher | <S> Student ------\n")
        while True:
            username = input("Enter your username: ").strip()
            password = masked_input("Enter your password: ")
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
    else:
        print("Invalid action! Pleace try again.")
    
users_data = load_users_data()  # Load existing user data

# Main program
def main():
    print("\n\t------ Welcome to the, Student Management System! ------\n")
    action = input("Choose an action:\n\t<L> Login  <S> Signup  <E> Exit\n").lower()
    if action in {"l", "s"}:
        login_signup(action)
    else:
        print(f"\t\t\t*** Exiting the program. Goodbye, Wisator! ***")

main()