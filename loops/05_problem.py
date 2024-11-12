# print the first non-repeated character from a string


name = "Sameer"

for char in name:
    if name.count(char) == 1:
        print("Char is: ", char)
        break



