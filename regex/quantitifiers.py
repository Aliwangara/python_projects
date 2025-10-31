
# * - asterick
    # “Match zero or more occurrences” of the previous character or pattern.

import re

text = "cat ct caaat caat"

asterick_matches = re.findall("ca*t", text)
# a* means: zero or more a’s

# So it matches:

# ct (zero as)

# cat (one a)

# caat (two as)

# caaat (three as)
print(asterick_matches)



# the plus - +
# “Match one or more occurrences” of the previous character or pattern.


plus_text = "cat ct caaat caat"

plus_match = re.findall("ca+t",plus_text)

# a+ means: one or more a’s

# So it will not match ct (because there’s no a).

print(plus_match)

# ? - question mark
# Match zero or one occurrence — the previous part is optional.
question_text = "color colour colouur"

question_match = re.findall("colou?r", question_text)

# u? means: u can appear 0 or 1 time

# So it matches both color and colour

# But not colouur (two u’s)


print(question_match)

# Asks the user to input a few words.

# Uses regex to find all words that contain one or more “a” letters.

# Prints the list and how many matches were found.

# 👉 Hint: You’ll need to use re.findall("a+", sentence_input, re.IGNORECASE)

words_input = input("Enter few words here:  ")

word_match = re.findall("a+", words_input,re.IGNORECASE)

print(word_match)



# Can you write a short Python program that:

# Asks the user for a word.

# Uses regex to check if that word has two or more repeating “o” letters together (like “food”, “zoo”, “goose”).

# Prints the matching “oo” parts if found.

# 👉 (Hint: "o+" means one or more o’s.)

# Would you like to try writing it yourself first?


search_input = input("Enter some words: ")

search_match = re.findall("o+", search_input,re.IGNORECASE)

print(search_match)




 
