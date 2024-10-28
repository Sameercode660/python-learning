'''
Write a program to find the mean, median and mode of a list of 10 numbers.

'''

import random

lst = list()

for x in range(20):
    lst.append(random.randrange(1000,9999))

print(lst)
sum = int()

for x in lst:
    sum += x

mean = sum / len(lst)

print(f'The mean of {mean}')

median = int()

if len(lst) % 2 == 0:
    median = (lst[int(len(lst)/2)-1] + lst[int((len(lst)+1)/2)]-1) / 2
else :
    median = lst[int((len(lst)+1)/2)-1]

print(f'median is {median}')
mode = int()
for x in lst:
    if lst.count(x) > 1:
        mode = x

if(mode > 1):
    print('mode is ', mode)
else:
    print('No mode exists!')
