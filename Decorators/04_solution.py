# Write a decorator validate_args that checks if all arguments passed to a function are positive integers. If not, raise a ValueError. Test it on a function add(a, b) that adds two numbers.

def validate_args(func):
    def wrapper(*args):
        for i in args:
            if not i >= 0 :
                return f"{args} are invalid arguments"
        return func(*args)
    return wrapper

@validate_args
def sum(a, b):
    return a + b

print(sum(-3, 2))
