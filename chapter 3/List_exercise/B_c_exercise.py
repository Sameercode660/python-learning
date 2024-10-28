# The following code snippet deletes element 30 and 40 from the list:

# num = [10, 20, 30, 40, 50]
# del(num[2:4])

# In which other way the same effect can be obtained

num = [10, 20, 30, 40, 50]

num[2:4] = []

print(num)

