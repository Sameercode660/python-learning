'''
Suppose a list contains several words. Write a program to create
list that contains first character of each word present in the first list

'''

lst = list(('sameer', 'sahil', 'suraj', 'amit', 'ajay', 'rahul'))

lstContainerFirstCharacter = list();

for name in lst:
    lstContainerFirstCharacter.append(name[0])

print(lst)
print(lstContainerFirstCharacter)