from functions import*
# add_user, get_user, order_users, list_users

print("Welcome to the database mini-application!")

switch = True
while switch == True:
    print("-"*100)
    print("""******************List of commands******************""")
    print("""
    # 1 list users
    # 2 add user
    # 3 get user by id
    # 4 order users by age
    # 5 add product
    # 6 list product
    # 7 update product
    # Enter the 'c' key to close the application 
    """)
    print("*"*50)
    command = input("Enter command: ")
    print("-"*100)
    if command == '1':
        list_users()
    
    elif command == '2':
        add_user()
    
    elif command == '3':
        get_user()
    
    elif command == '4':
        order_users()
    
    elif command == '5':
        add_product()

    elif command == '6':
        list_product()        

    elif command == '7':
        update_product()

    elif command == 'c':
        switch = False