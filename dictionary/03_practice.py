# How can you loop through a dictionary to print each key and its corresponding value?

dictionary = {
    "Name": "Sameer",
    "Rollno": 123,
    "Address": "Pune"
}

print(dictionary)

for key in dictionary:
    print(key, " = ", dictionary[key] )

print(dictionary)

# What methods are available to get all keys, all values, or all key-value pairs in a dictionary?

dictionary_keys = dictionary.keys()

print(dictionary_keys)

dictionary_value = dictionary.values()

print(dictionary_value)

dictionary_key_values = dictionary.items()

print(dictionary_key_values)

for key, value in dictionary_key_values:
    print(key, " = ", value)
