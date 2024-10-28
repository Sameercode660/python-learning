# list datatype
l1 = [1,2,3,4,5,6,7,8,9,10];

#tuple dataype
t1 = ('Sameer', 'is', 'a', 'good', 'boy')

#set container
s1 = {10, 12 , 12, 13}

#dictionary container
d1 = {
    'potable' : 'Which can be drinked',
    'eatable' : 'Which can be eaten',
    'abdomen' : 'stomach',
}

print(l1, " type of l1 is ", type(l1))
print(t1, " type of t1 is ", type(t1))
print(s1, " type of s1 is ", type(s1))
print(d1, " type of d1 is ", type(d1))

l1[0] = 120

print(l1[0])
print(l1)
print(d1['abdomen'])
