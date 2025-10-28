
# Opens a file named daily_log.txt in append mode

# Asks the user to input their daily learning summary

# Appends it to the file in this format:

daily_file  = "daily_log.txt"

with open(daily_file,'a',newline="") as f:
    day = int(input("Enter day: "))
    summary = input("Enter summary:  ").capitalize()
    f.write(f"Day {day}: {summary}\n")

with open(daily_file, 'r') as f:
    print("\n📘 Your Learning Progress:")
    print(f.read())