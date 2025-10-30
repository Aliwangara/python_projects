import re

email = input("Enter email:  ")


if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
    print("✅ Valid email")
else:
    print("Wrong email input missing an @")

# re.match - finds matching things in input
# re.findall - returns a list of all matches
# re.search - searches anywherein the string
# re.sub - replaces onething with the other
# re.split - splits the pattern

text = "Ali is a boy"

search = re.search("Ali", text)
print("Found: ", search.group())

# finding all numbers in a string 
new_text = "I have 2 apples and 5 oranges"
numbers = re.findall(r'\d+', new_text)
print(numbers)



# \d	Any digit (0–9)	“3”, “7”
# \w	Any letter, digit, or underscore	“abc_12”
# \s	Any whitespace (space, tab, newline)	“ ”
# ^	Start of string	^Hello → matches “Hello world”
# $	End of string	world$ → matches “Hello world”
# +	One or more occurrences	\d+ → “123”, “56”
# *	Zero or more occurrences	\w*
# {n}	Exactly n occurrences	\d{4} → “2025”