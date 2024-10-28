thislist = ['apple', 'mango', 'banana', 'guava']

thislist.remove('apple')
thislist.pop(1)

del thislist[0]

# del thislist
thislist.clear()

thislist[0:4] = ['Apple', 'Banana', 'Kiwi', 'Grapes', 'Guava']
thislist.insert(0, 'python')

for i in range(len(thislist)):
    if thislist[i] == 'Apple':
        index = i
        break
print('the index of apple is ', index)

thislist[index] = 'cython'

print(f'length of string {len(thislist)}')
print(thislist)

for x in thislist: 
    print(x)

print('-----')

for i in range(len(thislist)):
    print(thislist[i])

print('-----')

y = int()
while y < len(thislist):
    print(thislist[y])
    y += 1

lengthOfList = len(thislist)

print(type(lengthOfList))

print('-------------')

[print(x) for x in thislist]