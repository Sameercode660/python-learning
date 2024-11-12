# take the input from user until user enters the number from 1 to 10

while True:
    num = int(input("Enter a number: "))

    if num >= 1 and num <= 10:
        print("Correct")
        break
