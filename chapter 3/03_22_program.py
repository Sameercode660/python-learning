# program to tell whether a given number is prime or not 

num = int(input('Enter a number: '))

isPrime = True
for i in range(2, num):
    if(num % i == 0):
        isPrime = False
        break

if isPrime:
    print('Given number is prime')
else : 
    print('Given number is not a prime number!')