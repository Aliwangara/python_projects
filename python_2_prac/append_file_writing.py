# Create or reuse daily_journal.txt.

# Ask the user for 2 new entries.

# Open the file in append mode ('a') and add those entries.

# Read and print the entire file content.

journal = "append_journal.txt"

with open(journal,"a") as f:

    for i in range(1,3):
        new_append = input(f"Enter entry {i}:   ")
        f.write(new_append + "\n")

with open(journal, 'r') as f:
    print(f.read())