import re


# [] - Character sets let you match any one character from a group.

text = "bat bet bit bot but"
 
character_matches = re.findall('b[aeiou]t', text, re.IGNORECASE)
print(character_matches)


# 2️⃣ Character Range

second_text = "bat bet bit bot but bzt b9t"

second_match = re.findall('b[a-z]t', second_text,re.IGNORECASE)

# [a-z] → any lowercase letter

# [A-Z] → any uppercase letter

# [0-9] → any digit

# So b[a-z]t means:
# “b + any single lowercase letter + t”.

print(second_match)

# 3️⃣ Negated Set — [^ ]

# If you put a caret (^) inside the brackets, it means “not these characters”.

negated_text = "bat bet bit bot but b1t b$t"

negated_match = re.findall("b[^aeiou]t", negated_text, re.IGNORECASE)
print(negated_match)



