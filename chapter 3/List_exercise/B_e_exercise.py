'''
from the list given below

num1 = [10,20,30,40,50]

how will you create the list num2 containing

['A','B','C',10,20,30,40,50,'Y','Z']

'''

num1 = [10,20,30,40,50]

num1[:0] = ['A', 'B', 'C']

num1[len(num1):] = ['X', 'Y']
print(num1)