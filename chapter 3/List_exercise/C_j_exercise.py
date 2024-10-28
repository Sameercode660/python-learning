'''

A list contains 10 numbers. Write a program to eliminate all duplicates from the list


'''

lst = list((22,34,55,55,6,66,6,4,4,3,4))

uniqueList = list()

for element in lst:
    if element not in uniqueList:
        uniqueList.append(element)

print(lst)
print(uniqueList)