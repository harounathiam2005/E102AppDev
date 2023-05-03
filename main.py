from sqlfunc import *

user = input("Enter your username:")
password = input("Enter your password:")

while check_user_and_pass(connection, user, password) == False:
    print("")
    print("Username or password is incorrect. Please enter them again.")
    user = input("Username: ")
    password = input("Password: ")
    print("")

"""
get_data:
cursor = connection.cursor()
cursor.execute(f'SELECT balance FROM bank_accounts WHERE idbank_accounts = "{id}";')
item = get(cursor)
cursor.close()
print(item)
"""

print("Welcome...")
id = get_id(connection, password)

on = True
while on:
    print("")
    print("(1) Get balance")
    print("(2) Add to balance")
    print("(3) Change username")
    print("(4) Change password")
    print("(5) Add account")
    print("(6) Switch account")
    print("(7) Quit")
    print("")
    decision = input("What would you like to do? ")
    print("")
    if decision == "1":
        print(get_data(connection, 'balance', id))
    elif decision == "2":
        increment_balance(connection, id)
    elif decision == "3":
        check = input("Enter your password: ")
        while check_pass(connection, check) == False:
            print("")
            print("Password is incorrect. Please enter it again.")
            password = input("Password: ")
            print("")
        new_user = input("What would you like to change your username to?")
        print("")
        update(connection, 'user', new_user, id)
        print("Updated!")
    elif decision == "4":
        check = input("Enter your password: ")
        while check_pass(connection, check) == False:
            print("")
            print("Password is incorrect. Please enter it again.")
            password = input("Password: ")
            print("")
        new_pass = input("What would you like to change your password to?")
        print("")
        update(connection, 'pass', new_pass, id)
        print("Updated!")
    elif decision == "5":
        user = input("Enter a new username: ")
        print("")
        password = input("Enter a new password: ")
        print("")
        email = input("Enter your email: ")
        print("")
        insert_row(connection, user, password, email)
        print("Account created!")
    elif decision == "6":
        while check_user_and_pass(connection, user, password) == False:
            print("")
            print("Username or password is incorrect. Please enter them again.")
            user = input("Username: ")
            password = input("Password: ")
            print("")
        id = get_id(connection, password)
        print("")
        print("Current user: ", get_data(connection, 'user', id))
    elif decision == "7":
        print("Closing...")
        break
    else:
        print("Please choose from the displayed options. ")

connection.close()