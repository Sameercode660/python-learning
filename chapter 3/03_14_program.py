#creating a time delay in python

#import time module
import time
import os


#taking a loop for demonstration for each iteration
# 5 would be excluded in range 
for i in range(1,5):
    
    #print the number
    print(i)

    #creating time delay using sleep method
    time.sleep(2)

    #clearing the console screen using system('cls') method of os module
    os.system('cls')

