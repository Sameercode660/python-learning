# Write a decorator memoize that caches the results of a function so that if the function is called with the same arguments, the cached result is returned instead of recalculating.

# Test it on a recursive function fib(n) that computes the Fibonacci sequence.


def memoize(func):
    cache = {}
    print(cache)
    def wrapper(*args):
        if args in cache: 
            print(f"Cache hit for {args}: {cache[args]}")  
            return cache[args]
        
        print(f"Cache miss for {args}. Function executed.")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(7))
print(fib(7))
print(fib(7))
print(fib(7))
print(fib(7))