# Task: Build a program that manages student scores using CSV & JSON.

# Requirements:

# Ask user for a number of students.

# Collect each student’s name and score.

# Save the data to a CSV file.

# Convert the same data to JSON and save it as students.json.

# Read both files back and print the contents neatly.

import json
import csv

student_csv = "student.csv"
student_json = "students.json"

with open(student_csv, 'w',newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Score"])
    with open(student_csv, "a",newline="")as f:
        student_number = int(input("Enter number number of students you want to add:    "))
        for student in range(student_number):
            Name = input("Enter Students name:   ")
            Score = float(input("Enter students score:   "))
            writer.writerow([Name,Score])
            


with open(student_json, 'w') as f:
    json.dump(student_csv,f,)
    