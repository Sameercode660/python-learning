# Write a program to generate and store in a list 20 random numbers in the range 10 to 100. From this list delete all those entries which hace value between 20 and 50 print the remaining list

import random

thisList = []

for x in range(20):
    randomNum = random.randrange(10, 100)
    thisList.append(randomNum)

print(thisList)

for num in thisList:
    if num > 20 and num < 50:
        thisList.remove(num)

print(thisList)