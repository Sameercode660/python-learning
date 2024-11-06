# problem statement: write a python program for movie ticket pricing where price for person 18 or above is $12 and price for person below it is $8 doller and they all will get a discount of $2 is day is wednesday

day = "Wednesday"
age = 22

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

print(price)