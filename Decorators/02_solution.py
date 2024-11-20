# Problem 1: Basic Decorator
# Write a decorator called execution_time that calculates and prints the time taken by a function to execute. Test it on a function that calculates the sum of numbers from 1 to 10 million.

# Hint: Use the time module.

import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()

        return f"{func.__name__} takes {end - start} time to run"
    return wrapper   

@timer
def sumOfMillion():
    sum = 0
    for i in range(1, 10000000):
        sum += i

print(sumOfMillion())
