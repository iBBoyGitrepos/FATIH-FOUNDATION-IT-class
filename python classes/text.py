





# def user_dashboard(username, enter_by):
#     is_user = False
#     for user in users_data:
#         if user['user_name'] == username: 
#             is_user = True
#             # Initialize the content for the dashboard based on role
#             if user["role"] == 't': 
#                 is_teacher = 'N/A'
#                 role_content_heading = "Students: "
#                 role_content = ', '.join(user.get("students", []))
#                 role_menue = "<A> All Students|"
#             else:
#                 is_teacher = user["teacher"]
#                 role_content_heading = "Subjects: "
#                 role_content = ', '.join(user.get("subjects", []))
#                 role_menue = "<E> Examinations|"
                
#             # Print the user dashboard
#             print(f'''
#             \n\t\t \t  ------ Student Dashboard ({user["user_name"]}) ------ \n
#                -- MENUE --  |        Creat    |    Read    |    Update    |    Delete \n
#             {role_menue}   Name: {user["name"]} \t\tLast Name: {user["last_name"]} 
#             <N> New acount  |   Role: {user["role"]} \tAge: {user["age"]} \tTeacher Name: {is_teacher}
#             <L> Logout      |   {role_content_heading}
#             <B> Back        |   \t{role_content}

#             ''')
#             action = input("Enter your action: ").lower()
            
#             if action == 'a' and role_menue == "<A> All Students|":
#                 students_list()
#             elif action == 'e' and role_menue == "<E> Examinations|":
#                 user_dashboard()
#             elif action == 'n':
#                 login_signup('s')
#             elif action == 'l':
#                 main()
#             elif action == 'b':
#                 login_signup(enter_by)
#         else:
#             is_user 
            
#     if not is_user:
#         print(f"User {username} not found!")
