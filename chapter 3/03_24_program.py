# function in python 

def calculateGMean(a, b):
    mean = (a * b) / (a + b)
    print(mean)

a = int(input('Enter a number: '))
b = int(input('Enter second number: '))

calculateGMean(a, b)
