#match case statement in python

num = int(input('Enter a number: '))

match num:
    
    case 0: 
        print('Number is sezo')
    
    case _ if(num != 90):
        print('Number is not ninty')
    
    case _:
        print('Something went wrong')