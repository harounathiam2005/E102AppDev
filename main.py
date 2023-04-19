import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'new_schema', password = 'Sonic46!!')

cursor = connection.cursor()

testQuery = ("SELECT username FROM accounts")

cursor.execute(testQuery)

for item in cursor:
    print(item)

cursor.close()

connection.close()

