def factorial(num):
    if num == 0:
        return
    return num * factorial(num - 1)

num = input('Enter a number: ')
num = int(num);
print(factorial(num))