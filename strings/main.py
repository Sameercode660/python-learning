
name = "sameer"

print(name.capitalize())
print(name.casefold())
print(name.count('e'))
print(name.endswith('a'))

introduction = "My name is {} and i am living in {}"
city = "Pune"

print(introduction.format(name, city))

print(city.find('u'))

string = "123"

print(string.isalnum())
print(string.isalpha())
print(string.isdigit())
print(string.islower())
print(string.isupper())

listItems = ["Banana", "Apple", "Orange"]

print(", ".join(listItems))

string1 = "    how are you"

print(string1.lstrip())

string1 = "    how are you     "
print(string1.rstrip())

string1 = "    how are you     "
print(string1.strip())

string2 = "how are you and what are you doing"

print(string2.startswith("what"))

