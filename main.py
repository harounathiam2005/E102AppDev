import mysql.connector

def insert_row(connection, user, password, email, table):
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO {table} (username, password_hash, email) VALUES ("{user}", "hashed_{password}", "{email}");')
    connection.commit()
    cursor.close()

def remove_row(connection, id, table):
    print("debug", id, table)
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM {table} WHERE id{table} = {id};')
    connection.commit()
    cursor.close()

def clear_table(connection, table):
    print("debug", id, table)
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM {table};')
    connection.commit()
    cursor.close()

def dump_table(connection):
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    for item in cursor:
        print(item)
    cursor.close()

connection = mysql.connector.connect(user = 'root', database = 'new_schema', password = 'Sonic46!!')
table = 'accounts2'

insert_row(connection, 'hthiam', 'Sonic46!!', 'hthiam252', table)
dump_table(connection)

connection.close()

