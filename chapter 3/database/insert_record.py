import mysql.connector as connection

mydb = connection.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'db1'
)


cursor = mydb.cursor()

query = 'INSERT INTO book1(bookid, title, price) VALUES(%s, %s , %s)'

bookid = input('Enter book id: ')
title = input('Enter book Name: ')
price = input('Enter book price: ')

t = (bookid, title, price)

cursor.execute(query, t)

mydb.commit()