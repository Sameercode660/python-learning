'''
Given a list
lst = [10,25,4,12,3,8]
How will you check whether 30 is present in the list or not ?

'''
lst = [10, 25, 4, 12, 3, 8]


availibility = lst.count(30)

if availibility:
    print('Present in the list')
else: 
    print('Not Present in the List')
