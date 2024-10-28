import mysql.connector

mydb = mysql.connector.connect(

        host = 'localhost',
        user = 'root',
        password = '123456',
        database = 'db1'
)

cursor = mydb.cursor();

cursor.execute("SELECT * FROM BOOK1")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
 