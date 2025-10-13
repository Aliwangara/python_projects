# Goal:

# Build a program that uses all the topics you’ve covered:
# ✅ Variables & Data Types
# ✅ Loops & Conditionals
# ✅ Functions
# ✅ File Handling (Text & CSV)
# ✅ Object-Oriented Programming (OOP: classes, inheritance, encapsulation, etc.)
# ✅ Polymorphism, Class Methods, Static Methods

# 💼 Project: Student Management System
# 🧾 Requirements:

# You’ll build two classes:

# 1️⃣ Class: Student

# Private attributes:

# __name

# __age

# __score

# Class attributes:

# __school_name = "Bright Future Academy"

# __student_count = 0

# Methods:

# __init__(self, name, age, score) → initialize and increment student count

# get_name(), get_age(), get_score()

# student_info() → print name, age, score, and school

# @classmethod total_students(cls) → print total students

# @staticmethod is_valid_score(score) → returns True if 0 ≤ score ≤ 100

# 2️⃣ Class: Graduate(Student)

# A subclass of Student.

# Extra attribute:

# __degree

# Overrides:
# student_info() → includes degree name when printing.

# 3️⃣ File Handling Requirements

# When a student (or graduate) is added:

# Their data must be saved to a CSV file → students.csv

# Columns: Name, Age, Score, Status, Degree

# 👉 Status = "Pass" if score ≥ 50, else "Fail".
# 👉 Degree = "N/A" for normal students.

# After all entries:

# Read the CSV file and print the data like this:

# Ali (Age: 21) scored 85 — Status: Pass — Degree: N/A
# George (Age: 22) scored 45 — Status: Fail — Degree: BSc Computer Science

# ⚙️ Program Flow

# Ask the user:
# How many students do you want to add?

# For each student:

# Ask for name, age, score

# Validate using Student.is_valid_score()

# Ask if they’re a graduate:
# If yes → also ask for degree.
# Create either a Student or Graduate object.
# Save data to CSV (students.csv).
# After all entries:
# Show all records from the CSV file.
# Show total students using Student.total_students().