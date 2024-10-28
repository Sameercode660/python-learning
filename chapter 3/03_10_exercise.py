# calculator using elif ladder 


num1 = int(input('Enter first number: '))
operator = input('Enter the oprator: ')
num2 = int(input('Enter second number: '))

if operator == '+':
    print(num1, ' + ', num2 , ' = ', num1 + num2)

elif operator == '-':
    print(num1, ' - ', num2 , ' = ', num1 - num2)

elif operator == '*':
    print(num1, ' * ', num2 , ' = ', num1 * num2)
    
elif operator == '/':
    print(num1, ' / ', num2 , ' = ', num1 / num2)

else : 
    print('Something went wrong!')