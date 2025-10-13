# Student Performance Tracker
# 🎯 Goal

# Build a program that:

# Stores student details in a CSV file.

# Validates their score.

# Automatically classifies them as Pass or Fail.

# Displays all records neatly at the end.

# 🧾 Requirements

# File name: performance.csv

# Columns: Name, Age, Score, Status

# Ask the user how many students to add.

# For each student:

# Ask for their name, age, and score.

# If the score:

# >= 50 → status = "Pass"

# < 50 → status = "Fail"

# If score is outside 0–100 → skip and show "Invalid score!"

# Save all valid data to the CSV file.

# Finally, read and print all records like this:

# Ali (Age: 21) scored 85 — Status: Pass
# George (Age: 20) scored 47 — Status: Fail

# 💡 Hint

# You’ll use:

# csv.writer() to write to file

# csv.reader() to read from file

# Conditional logic (if/else) for score validation and pass/fail

import csv

student_performance_file = "performance.csv"

with open(student_performance_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "score","status"])

with open(student_performance_file,"a", newline="") as f:
    writer = csv.writer(f)
    students_number_input = int(input("Enter number of students to add:  "))

    for student in range(students_number_input):
        name = input("Enter name of the student:  ").capitalize()
        age = int(input("Enter Age of the student:  "))
        score = float(input("Enter students score:  "))

        if 50 <= score <=100:
            status = "Pass"
            writer.writerow([name,age,score,status])
        elif score <50 and score > 0:
            status = "Fail"
            writer.writerow([name,age,score,status])
        else:
            print("Invalid score!")

with open(student_performance_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        if len(row) !=4:
            continue
    for name , age, score, status in reader:
        # Ali (Age: 21) scored 85 — Status: Pass
        print(f"{name} (Age:{age}) scored {score} - status: {status}")

