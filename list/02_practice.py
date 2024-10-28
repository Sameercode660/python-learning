
def modifyList(list1):
    l = []

    for i in list1: 
        if even(i):
            l.append(i**2)
    return l

def even(i):
    return i % 2 == 0


even_number = [x for x in range(1, 101)]

print(modifyList(even_number))
