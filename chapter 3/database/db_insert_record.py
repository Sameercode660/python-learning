import mysql.connector

mydb = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'db1'
)

cur = mydb.cursor()

query = 'INSERT INTO book1(bookid, title, price)  VALUES(%s, %s, %s)'

bookid = input('Enter book id: ')
title = input('Enter the title of this book: ')
price = input('Please mention the price of this book: ')

b1 = (bookid, title, price)

cur.execute(query,b1);

mydb.commit()