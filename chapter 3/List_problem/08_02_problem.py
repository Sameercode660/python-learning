#1. Create a list of 5 odd numbers
odd = [1,3,5,7,9]
print(odd)

#2. Create a list of 5 even numbers
even = [2,4,6,8,10]
print(even)

#3. Combine two list 
odd.extend(even)
print(odd)

#4. Add prime number 11, 27, 29 at the beginning of the combined list
odd = [11, 27, 29] + odd
print(odd)

# 5. Report how many elements are present in the list 
print(len(odd))

# 6. replace last 3 number in the list with 100, 200, 300
odd[-3:] = [100, 200, 300]
print(odd)

# 7. Delete all the numbers in the list
odd.clear()
print(odd)

# 8. Delete the list
del odd
print(odd)
