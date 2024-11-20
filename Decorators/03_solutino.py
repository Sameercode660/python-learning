# Problem 2: Parameterized Decorator
# Create a decorator called repeat that takes an argument n and makes the decorated function execute n times.

# Example:

# python
# Copy code
# @repeat(3)
# def say_hello():
#     print("Hello!")

def repeat(n):
    def inner_func(func):
        def wrapper(*args):
            for i in range(1, n + 1):
                func()
        return wrapper
    return inner_func


@repeat(3)
def say_hello():
    print("Hello!")

say_hello()