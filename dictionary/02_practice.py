 # How can you remove a key-value pair from a dictionary

dictionary = {
    "Name": "Sameer",
    "Rollno": 123
}

print(dictionary)

dictionary.pop("Rollno")

print(dictionary)

del dictionary["Name"]

print(dictionary)