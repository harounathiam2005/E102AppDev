import mysql.connector

def insert_row(connection, user, password, email):
    cursor = connection.cursor()
    #Encrypt class (?) -->
    cursor.execute(f'INSERT INTO bank_accounts (user, pass, email, balance) VALUES ("{user}", "{password}", "{email}", 0);')
    connection.commit()
    cursor.close()

def remove_row(connection, id):
    print("debug", id)
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM bank_accounts WHERE idbank_accounts = {id};')
    connection.commit()
    cursor.close()

def clear_table(connection):
    print("debug", id)
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM bank_accounts;')
    connection.commit()
    cursor.close()

def dump_table(connection):
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM bank_accounts;')
    for item in cursor:
        print(item)
    cursor.close()

def get_id(connection, password):
    cursor = connection.cursor()
    cursor.execute(f'SELECT idbank_accounts FROM bank_accounts WHERE pass = "{password}";')
    id = get(cursor)
    cursor.close()
    return id

def get_data(connection, field, id):
    cursor = connection.cursor()
    cursor.execute(f'SELECT {field} FROM bank_accounts WHERE idbank_accounts = "{id}";')
    item = get(cursor)
    cursor.close()
    return item

def get(cursor):
    for i in cursor:
        for x in i:
            return x

def update(connection, field, new_value, id):
    cursor = connection.cursor()
    cursor.execute(f'UPDATE bank_accounts SET {field} = "{new_value}" WHERE idbank_accounts = "{id}";')
    connection.commit()
    cursor.close()

def increment_balance(connection, id):
    value = input("How much would you like to add to your account? ")
    print("")
    new_balance = int(get_data(connection, 'balance', id)) + int(value)
    update(connection, 'balance', f'{new_balance}', id)
    print(f"Your new balance is {new_balance}.")

def check_user_and_pass(connection, user, password):
    cursor = connection.cursor()
    cursor.execute(f'SELECT COUNT(*) FROM bank_accounts WHERE pass = "{password}";')
    pass_check = get(cursor)
    cursor.execute(f'SELECT COUNT(*) FROM bank_accounts WHERE user = "{user}";')
    user_check = get(cursor)
    cursor.close()
    if pass_check == 1 and user_check == 1:
        return True
    else:
        return False

def check_pass(connection, password):
    cursor = connection.cursor()
    cursor.execute(f'SELECT COUNT(*) FROM bank_accounts WHERE pass = "{password}";')
    pass_check = get(cursor)
    cursor.close()
    if pass_check == 1:
        return True
    else:
        return False

def get_pass_mutate(password):
    pass_arr = [i for i in password]
    if len(pass_arr) == 1:
      pass_arr[0] = "*"
    elif len(pass_arr) <= 2:
      pass_arr[1] = "*"
    else:
      for i in range(1, len(pass_arr) - 1):
        pass_arr[i] = "*"
    return "".join(pass_arr)


connection = mysql.connector.connect(user = 'root', database = 'new_schema', password = 'Sonic46!!')