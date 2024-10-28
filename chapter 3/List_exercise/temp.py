import random

lst = []

for i in range(20):
    num = random.randrange(1,100)
    lst.append(num)

print(lst)

print(lst.count(lst[0]))