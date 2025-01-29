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