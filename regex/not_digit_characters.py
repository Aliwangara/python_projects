import re

# \D → Not a digit

sentence = input("Enter something with numbers: ")

not_digit = re.findall(r"\D+", sentence)
print(not_digit)

# 🔹 2. \W → Not a word character

# Matches anything that’s not a letter, digit, or underscore.

not_word = re.findall(r"\W+", sentence)
print(not_word)

# 🔹 3. \S → Not a space

# Matches everything except spaces, tabs, and newlines.

not_space = re.findall(r"\S+", sentence)
print(not_space)