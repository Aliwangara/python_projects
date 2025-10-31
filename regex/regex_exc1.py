# Write a Python program that:

# Asks the user to enter a sentence.

# Uses regex to check if the word "Python" appears in it.

# Prints "Yes, found!" or "Not found!".

import re
sentence_input = input("nter a sentence:  ")

word_search = re.search("python", sentence_input,re.IGNORECASE)

if word_search:
    print(f"{word_search.group()} is available")
else:
    print("Not available")

# Asks for a sentence.

# Finds all occurrences of the word "hello".

# Prints the list and total count.

occurrence_input = input("Enter a sentence: ")

findall = re.findall("hello", occurrence_input)
print(findall)
print("Occurrence: ", len(findall))