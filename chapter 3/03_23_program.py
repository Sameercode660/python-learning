# sum of first n natural number using while loop

num = int(input('Enter a number: '))

i = 1
sum = 0
while i <= num:
    if(str(num).endswith('0')):
        continue;
    sum += int(num) 
    i += 1

# sum = (num * (num + 1)) / 2

print(sum)