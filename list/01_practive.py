# Write a Python function to create a list of the first n integers, starting from 1. Use this list to find the sum, average, maximum, and minimum values.


def createList(n):
    l1 = []

    for i in range(n):
        l1.append(i)
    
    return l1

def sumOfList(list1):
    sum = 0

    for value in list1:
        sum += value
    
    return sum

def maximum(list1): 
    maximum = 0

    for value in list1:
        if(maximum < value):
            maximum = value
    return maximum

def minimum(list1):
    minimum = 0

    for value in list1:
        if(minimum > value):
            minimum = value
    return minimum

def average(list1):
    sum = 0

    for value in list1:
        sum += value

    return sum / len(list1)


list1 = createList(10)

print(list1)
print(minimum(list1))
print(maximum(list1))
print(average(list1))
print(sumOfList(list1))

