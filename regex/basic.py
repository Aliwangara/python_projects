import re

text = "My name is Ali"

search = re.search("Ali", text)

if search:
    print(search.group())
else:
    print("not found")

findall = "boy girl boy girl boy child boy"

print(re.findall("boy", findall))

# Write a Python program that:

# Asks the user to enter a sentence.

# Uses regex to check if the word "Python" appears in it.

# Prints "Yes, found!" or "Not found!".
