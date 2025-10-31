# . - matches any single characters eg:

import re

text = "cat, cot, cut, cbt, ctt"

matches = re.findall("c.t", text)

print(matches)

#  this matches names that start with c and ends with t; the . represents the middle character


# 2. ^ Caret
# Matches sentences at the beginning of a string

caret_text = "Python is great. I love Python."

matches_caret = re.findall("^Python", caret_text)

print(matches_caret)

# dollarsign $ - Matches at the end of a string

text_dollar = "I am learning Python"

match_dollar = re.findall("Python$", text_dollar)
print(match_dollar)




# Asks the user for a sentence.

# Checks if the sentence starts with “Hello” and ends with “bye”.

# Prints messages accordingly (e.g., “Starts with Hello”, “Ends with bye”).


sentence_input = input("Enter input:  ")

match_start = re.findall("^Hello", sentence_input, re.IGNORECASE)
match_end = re.findall("bye$", sentence_input, re.IGNORECASE)

print(f"Starts with {match_start}, Ends with {match_end}")









