'''
Suppose a list contains positive and negative numbers. Write a program to create two lists-one containing positive numbers
and another containing negative numbers.

'''

lst = [-1,-4,7,8,-7,9,4,-8,7,3,4,-2]

negativeList = []

for num in lst:
    if num < 0:
        negativeList.append(num)
        lst.remove(num)

print(lst)
print(negativeList)