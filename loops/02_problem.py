# calculate the sum of even number from a list

numbers = [1,2,3,4,5,6,7,8,9,10]
sum = 0

for num in numbers:
    if num % 2 == 0:
        sum += num
print("Sum of all even numbers is: ", sum)
