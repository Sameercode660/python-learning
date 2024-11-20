
# Problem 4: Chaining Multiple Decorators
# Create two decorators:

# uppercase: Converts the string returned by a function to uppercase.
# add_exclamation: Adds an exclamation mark (!) at the end of the string returned by a function.
# Use both decorators on a function greet(name) that returns "Hello, {name}".


def add_exclamation(func):
    def wrapper(*args):
        result = func(*args)
        return result + "!"
    return wrapper

def uppercase(func):
    def wrapper(*args):
        result = func(*args)
        return result.upper()
    return wrapper
 
@add_exclamation
@uppercase
def greet(name):
    return f"Hello, {name}"

print(greet("Sameer"))
 