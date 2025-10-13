# Daily Journal Writer”
# 🎯 Goal

# Create a program that:

# Writes 3 journal entries to a text file.

# Reads the file and displays each entry clearly.

# 🧾 Instructions

# Create a file called daily_journal.txt

# Ask the user for 3 lines of text (journal entries).

# Write each entry on a new line in the file.

# Read the file and print each line like this:

journal_file = "daily_journal.txt"

with open(journal_file, "w") as f:
    for i in range(1,4):
     entry = input(f"Enter Journal entry{i}:   ").title()
     f.write(f"{entry}\n")

with open(journal_file,"r") as f:
   for i, line in enumerate(f,1):
      print(f"{i}. {line}")