# Mini Challenge for You

# Create a program that:

# Writes 4 favorite quotes to a file named quotes.txt.

# Reads and prints each line with line numbers (like a list).

quote = "quotes.txt"

with open(quote, 'w') as f:
    f.write("Learn Python\n")
    f.write("Practice daily\n")
    f.write("Stay consistent\n")
    f.write("Rest\n")

with open(quote,"r") as f:
    for i,  line in enumerate(f,1):
        print(f"{i}. {line.strip()}")