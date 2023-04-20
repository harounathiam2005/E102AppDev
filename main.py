import mysql.connector

def insert(connection, user, password, email, table):
    print("debug", user , password , email)
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO {table} (username, password_hash, email) VALUES ("{user}", "hashed_{password}", "{email}");')
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

insert(connection, 'hthiam2', 'Sonic55', 'ht@gmail.com', table)
dump_table(connection)

connection.close()

