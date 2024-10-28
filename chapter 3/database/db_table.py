import mysql.connector

mydb = mysql.connector.connect(

    host ='localhost',
    user ='root',
    password = '123456',
    database = 'web1'
)

cur = mydb.cursor()

query = '''CREATE TABLE  w1(
            name integer(50),
            email varchar(50),
            password integer(50)
        )'''

cur.execute(query)