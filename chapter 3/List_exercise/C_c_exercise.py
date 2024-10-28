'''
Suppose a list has 20 number write a program that removes all duplicates from this list.

'''

import random 

lst = []

for x in range(20):
    lst.append(random.randrange(1,100))

print(lst)

for y in lst:
    if lst.count(y) > 1:
        lst.remove(y)

print(lst)