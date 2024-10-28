"""
Suppose a list contains 20 integer gererated randomly. Recieve a number
from the keyboard and report position of all occurrences of this number in 
the list.

"""

import random

lst = []

number = int(input('Enter a number: '))

for x in range(20):
    lst.append(random.randrange(1,100))

print(lst)

for y in range(20):
    if int(lst[y]) == number:
        print(f"The position of entered number in list is {y+1} position")
        break;
else:
    print('Number is not present in the list')

print(list())
