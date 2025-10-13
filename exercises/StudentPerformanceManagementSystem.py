# Create a Python program that can:

# Read and write student data from a CSV file

# Use OOP to represent each student

# Analyze performance (pass/fail, average, top student, etc.)

# Handle errors gracefully (e.g., missing file, invalid input)

# Display a summary report

# 🧩 FEATURES TO IMPLEMENT
# 1️⃣ Class Design

# Create a Student class with:

# name

# age

# score

# status (pass/fail)

# Include methods:

# is_pass() → returns True if score ≥ 50

# __str__() → returns student info neatly formatted

# 2️⃣ File Handling

# Use a CSV file named students.csv with columns:

# Name,Age,Score
# Ali,17,80
# Maria,18,45
# John,16,70
# Lina,17,30


# Your program should:

# Read data from students.csv

# Create a Student object for each row

# Store them in a list

# 3️⃣ Exception Handling

# Use try/except for:

# File not found errors

# Invalid numeric data (non-numeric score or age)

# Division by zero (if calculating averages)

# Example:

# try:
#     with open("students.csv", "r") as f:
#         ...
# except FileNotFoundError:
#     print("Error: students.csv not found.")

# 4️⃣ Functions (Procedural + OOP Mix)

# Write helper functions:

# get_average_score(student_list)

# get_top_student(student_list)

# get_fail_count(student_list)

# 5️⃣ Reporting

# After processing:
# ✅ Print:

# Total students: 4
# Passed: 2
# Failed: 2
# Average Score: 56.25
# Top Student: Ali (80)
# Lowest Score: Lina (30)


# ✅ Also write a report file report.txt summarizing the same information.


import csv
class Student:

    def __init__(self,name,age,score,status):
        self.__name =name
        self.__age = age
        self.__score = score
        self.__status = status
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_score(self):
        return self.__score
    @staticmethod
    def is_pass(score):
        return score >= 50
    def student_info(self):
        print(f"Name: {self.get_name()}, Age:{self.get_age()}, Score: {self.get_score()}")

students_file = "stds.csv"

with open(students_file,'w',newline="")as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Age","Score"])

with open(students_file, 'a',newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Ali",17,80])
    writer.writerow(["Maria",18,45])
    writer.writerow(["John",16,70])
    writer.writerow(["Lina",17,30])


try:
    with open(students_file,'r') as f:
        reader = csv.DictReader(f)
        reader_list = list(reader)
except FileNotFoundError:
    print("File not found")