# CSV- comma separated values

# Student Grades Manager
# 🎯 Goal

# You’ll create a small program that:

# Saves student names, ages, and scores into a CSV file.

# Then reads and displays all the student records nicely.

# 🧾 Requirements

# Create a file called grades.csv.

# Ask the user how many students they want to add.

# For each student:

# Ask for name, age, and score.

# Save them to the file.

# After saving, read and display each record as:

# Ali (Age: 21) scored 85


# (Bonus 🧠) — if the score is not between 0 and 100, skip saving that student and show an error message.

import csv

grade_file = 'grades.csv'

with open(grade_file,"w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Score"])
    student_number_input = int(input("Enter number of students you want to add:  "))

    for student in range(student_number_input):
        name = input("Enter name of student:   ")
        age = int(input("Enter Age of student:  "))
        score = float(input("Enter student score:  "))
        writer.writerow([name,age,score])

with open(grade_file,'r') as f:
    reader = csv.reader(f)

    next(reader)

    for i , name,age,score in enumerate(reader, 1):
        print(f"{i}. {name}, (Age:{age}), Scored:{score}")


