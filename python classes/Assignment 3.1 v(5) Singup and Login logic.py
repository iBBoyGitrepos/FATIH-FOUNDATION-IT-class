import msvcrt

# User data storage
users_data = {
    "IB": {
        "name": "ibrahim",
        "password": "777",
    },
    "KA": {
        "name": "kaab",
        "password": "666",
    }
}

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

# Main program
user_name = ""
password = ""
stage = "home page"

while True:
    if stage == "home page": 
        print("\n\t------ Welcome to the Home Page! ------\n")
        while stage == "home page":
            action = input("Choose an action:\n\t<L> Login  <S> Signup  <E> Exit\n").lower()

            if action in {"l", "s"}:
                while stage == "home page":
                    user_name = input("Enter your username: ").strip()
                    password = masked_input()

                    if action == "s":  # Signup
                        if user_name not in users_data:
                            name = input("Enter your name: ").strip()
                            users_data[user_name] = {
                                "name": name,
                                "password": password,
                            }
                            print(f"Signup successful! Welcome, {name}.")
                            stage = "logged"
                        else:
                            print(f"Username '{user_name}' is already taken. Try another!")

                    elif action == "l":  # Login
                        if user_name in users_data and users_data[user_name]["password"] == password:
                            print(f"Login successful! Welcome back, {users_data[user_name]['name']}.")
                            stage = "logged"
                        else:
                            print("Invalid username or password. Please try again.")
            elif action == "e":  # Exit
                print("\t\t\t*** Exiting the program. Goodbye! ***")
                stage = "exited"
            else:
                print("Invalid action. Please choose Login, Signup, or Exit.\n")
         
    if stage == "logged": 
        print("\n\t------ Welcome to the Dashboard! ------\n")
        while stage == "logged":
            action = input("Choose an action:\n\t<L> Logout  <S> Signout  <G> Go Back  <E> Exit\n").lower()

            if action == "s":  # Signout
                print(f"Account '{user_name}' has been deleted. Goodbye, {users_data[user_name]['name']}.")
                del users_data[user_name]
                stage = "home page"

            elif action == "l":  # Logout
                print(f"Logged out. Goodbye, {users_data[user_name]['name']}.")
                stage = "home page"

            elif action == "g":  # Go Back
                stage = "home page"

            elif action == "e":  # Exit
                print(f"\t\t\t*** Exiting the program. Goodbye, {users_data[user_name]['name']}! ***")
                stage = "exited"

            else:
                print("Invalid action. Please choose Logout, Signout, Go Back, or Exit.\n")

    if stage == "exited":
        break
