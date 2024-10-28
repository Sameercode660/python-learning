thisList = ['Anil', 'Amol', 'Aditya', 'Avi', 'Alka']

#1. insert a name 'Anuj' before 'Aditya'
thisList.insert(2, 'anuj')
print(thisList)

#2. Append a name 'Zulu'
thisList.append('Zulu')
print(thisList)

#3.Delete 'Avi' from the list
del thisList[4] 
print(thisList)

#4. Replace 'Anil' with 'AnilKumar'
#method 1
# thisList[0] = 'AnilKumar'
# print(thisList)

#method 2
for x in range(len(thisList)):
    if 'Anil' == thisList[x]:
        thisList[x] = 'AnilKumar'

print(thisList)

#5 print the sorted list
thisList.sort()
print(thisList)

#6 print reversed sorted list
thisList.reverse()
print(thisList)

