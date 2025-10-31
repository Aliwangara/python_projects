# Write a Python program that:

# Asks the user for a few words.

# Finds all 3-letter words that:

# start with b

# end with t

# and have a vowel in the middle.

# Prints the matches.

import re

user_words = input("Enter a few words: ")

user_match = re.findall("b[aeiou]t",user_words,re.IGNORECASE)
print(user_match)


