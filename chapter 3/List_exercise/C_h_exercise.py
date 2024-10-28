''' 
A list contains only positive and negative integer,
write a program to obtain the number of negative present in the list.

'''

lst = list((-2,4,-5,5,6,-2,-7,9,-3))

countNegative = int(0)

for num in lst:
    if num < 0:
        countNegative += 1;

print(f'The nummber of negative number is {countNegative}')
