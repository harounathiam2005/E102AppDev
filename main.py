from sqlfunc import *
from menu import menu

print(get_data(connection, 'balance', 1))

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
print(id)

print("")
on = True
while on:
    print("")
    print("(1) Get balance")
    print("(2) Add to balance")
    print("(3) Change username")
    print("(4) Change password")
    print("(5) Add account")
    print("(6) Switch account")
    print("(7) Transfer balance")
    print("(8) Quit")
    print("")
    decision = input("Tell me, what would you like to do? ")
    print("")
    if decision == "1":
        balance = get_data(connection, 'balance', id)
        print(balance)
    elif decision == "2":
        increment_balance(connection, id)
    elif decision == "3":
        pass
    elif decision == "4":
        pass
    elif decision == "5":
        pass
    elif decision == "6":
        pass
    elif decision == "7":
        pass
    elif decision == "8":
        print("Closing...")
        print("")
        break
    else:
        print("Please choose from the displayed options. ")
        print("")

connection.close()