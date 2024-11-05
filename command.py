from functions import add_user, get_user, order_users, list_users

print("Welcome to the database mini-application!")
print("commands")
print("""
# 1 list users
# 2 add user
# 3 get user by id
# 4 order users by age
# Enter the 'c' key to close the application""")

switch = True
while switch == True:
    command = input("Enter command: ")
    if command == '1':
        list_users()
    
    elif command == '2':
        add_user()
    
    elif command == '3':
        get_user()
    
    elif command == '4':
        order_users()

    elif command == 'c':
        switch = False