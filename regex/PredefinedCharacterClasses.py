import re

# \d → gets Digits (0–9)

d_text = "Room 12 is on floor 3, code 4567"

d_match = re.findall(r"\d+", d_text)
print(d_match)

# 2️⃣ \w → gets Word Characters

w_text = "Hi_123 there!"

w_match = re.findall(r"\w+", w_text)
print(w_match)

# 3️⃣ \s → gets Whitespace Characters

s_text = "Hello world this is regex"

s_match = re.findall(r"\s",s_text)
print(s_match)


# Asks the user to enter any sentence.

# Finds and prints:

# All numbers (\d+)

# All words (\w+)

# All spaces (\s)

# Prints how many of each were found.

user_sentence = input("Enter any sentence:  ")

digit_match = re.findall(r"\d+", user_sentence)
print(digit_match)
word_match = re.findall(r"\w+",user_sentence )
print(word_match)
space_match = re.findall(r"\s", user_sentence)
print(space_match)