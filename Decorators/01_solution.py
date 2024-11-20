# Write a decorator that measures the time a function takes to execute

def decorator(func):
    def wrapper(*args, **kwargs):
        print("How are you")
        return func()
    return wrapper

@decorator
def hello():
    print("Hello, world")
    return "I'm called"

 
print(hello())