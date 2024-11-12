# find the factorial of a number using while loop

num = 1
factorial = 1

while num > 0:
    factorial *= num
    num -= num

print(factorial)