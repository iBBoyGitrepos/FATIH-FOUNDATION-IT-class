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
                # Move cursor back, erase character, move back again
                print("\b \b", end="", flush=True)
        else:
            password += char.decode("utf-8")
            print("*", end="", flush=True)
    print()  # Move to the next line
    return password

user_name = ""
password = ""
stage = "home page"

while True:
    if stage == "home page": 
        print("\n\t------Welcom! in our Home page.------\n")
        while  stage == "home page":
            action = input("press the action key! which would like to do? \n\t <L>ogin  <S>ign-up  <E>xit\n")

            if action == "l" or action == "s":
                while stage == "home page":
                    user_name = input("enter your user name: ")
                    password = masked_input()

                    if action == "s":
                        if not user_name in users_data.keys():
                            name = input("enter your name: ")

                            users_data[user_name] = {
                                "name": name,
                                "password": password,
                            }

                            print(f"Signup successful! Welcome, {name}.")
                            stage = "logged"
                        else:
                            print(f"That '{user_name}' username is taken. Try another!")
                    elif action == "l":
                        if user_name in users_data.keys():
                            if users_data[user_name]["password"] == password:
                                print(f"Login successful! Welcome back, {users_data[user_name]["name"]}.")
                                stage = "logged"
                            else:
                                print("Invalid username or password. Please try again.")
                        else:
                            print("Invalid username or password. Please try again.")
            elif action == "e":
                print("\t\t\t***Exiting the program. Goodbye!***")
                stage = "exited"
            else:
                print("Invalid action. Please choose Login, Signup, or Exit.\n")
         
    if stage == "logged": 
        print("\n\t------Let's! Redirect to the dashboard.------\n")
        while  stage == "logged":
            action = input("press the action key! which would like to do?\n    <L>ogout <S>ingout <G>oback <E>xit\n")

            if action == "s":
                print(f"Singout your '{user_name}' acount. Goodbye! {users_data[user_name]["name"]}.")
                del users_data[user_name]
                stage = "home page"
            elif action == "l":
                print(f"Logout from dashboard. Goodbye! {users_data[user_name]["name"]}.")
                stage = "home page"
            elif action == "g":
                stage = "home page"
            elif action == "e":
                print(f"\t\t\t***Exiting the program. Goodbye! {users_data[user_name]["name"]}***")
                stage = "exited"
            else:
                print("Invalid action. Please choose Logout, Singout, Goback, or Exit.\n")