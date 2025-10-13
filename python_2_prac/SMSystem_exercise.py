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

import csv

# class Student:
#     __school_name = "Bright Future Academy"
#     __student_count = 0
#     def __init__(self,name,age,score):
#         self.__name = name
#         self.__age = age
#         self.__score = score
#         Student.__student_count +=1

#     def get_name(self):
#             return self.__name
#     def get_age(self):
#             return self.__age
#     def get_score(self):
#             return self.__score
#     def get_status(self):
#            if 0 <= self.get_score() <= 100:
#             return "Pass" if self.get_score() >= 50 else "Fail"
#            else:
#                  return "Invalid"
           
#     def student_info(self):
#           print(f"Name: {self.get_name()}, Age: {self.get_age()}, Score: {self.get_score()}, School: {Student.__school_name}")

#     @classmethod
#     def total_students(cls):
#           print(f"Total Student: {cls.__student_count}") 
#     @staticmethod
#     def is_valid_score(score):
#           return  0 <= score <= 100
    
# class Graduate(Student):
#     def __init__(self, name, age, score,degree):
#             super().__init__(name, age, score)
#             self.__degree = degree
#     def get_degree(self):
#           return self.__degree
#     def student_info(self):
#           super().student_info()
#           print(f"Certification: {self.get_degree()}")
        
# # File Handling:

students_info = "students.csv"

# with open(students_info, "w", newline="") as f:
#       writer = csv.writer(f)
#       writer.writerow(["name","age","score","status","degree"])

# count = int(input("How many students do you want to add:   "))

# for i in range(count):
#     name = input(f"Enter name of student {i+1}:  ")
#     age = int(input(f"Enter {name}'s age:  "))
#     score = float(input(f"Enter {name}'s Score:    "))

#     if not Student.is_valid_score(score):
#           print(f"Invalid Score skipping {name}")
#           continue
    
#     is_grad = input("Is this student a graduate? (yes/no):     ").lower()

#     if is_grad == "yes":
#         degree = input("Enter degree:  ")
#         student = Graduate(name,age,score,degree)
#         degree_field = degree
#     else:
#         student = Student(name, age, score)
#         degree_field = "N/A"




#     with open(students_info,'a',newline="") as f:
#       writer = csv.writer(f)
#       writer.writerow([student.get_name(),student.get_age(), student.get_score(),
#                          student.get_status(), degree_field])
      


# print(f"====== Students Records ======")
# with open(students_info, 'r') as f:
#       reader = csv.reader(f)
#       next(reader)
#       for name,age,score,status,degree in reader:
#             print(f"{name} (Age: {age}) scored {score} — Status: {status}, degree: {degree}")

# Student.total_students()

# Student Data Analyzer”

# 🎯 Goal:
# Take your existing students.csv file and build a program that:

# Reads all data from it.

# Counts and displays:

# Total students

# Number of Pass and Fail students

# Number of graduates vs regular students

# Finds and prints:

# Highest scoring student

# Lowest scoring student

# Average score of all students
with open(students_info, "r") as f:
    readable = csv.DictReader(f)
    list_readable = list(readable)
    total_students = len(list_readable)
    print(total_students)
    pass_number =0
    fail_number = 0
    for item in list_readable:
        item_pass_or_fail = item["status"]

        if item_pass_or_fail =="Pass":
            pass_number +=1
        elif item_pass_or_fail == "Fail":
            fail_number +=1
    print(f"Pass: {pass_number}")
    print(f"Failed: {fail_number}")

    graduate_students = 0
    regular_students = 0

    for edu in list_readable:
        education_level = edu["degree"]
        if education_level == "N/A":
            regular_students+=1
        elif education_level != "N/A":
            graduate_students +=1
    print(f"Graduates: {graduate_students}")
    print(f"Regular Students: {regular_students}")

    #Highest scoring students

    top_student =  max(list_readable, key=lambda x:x['score'])
    #Lowest student
    lowest_student = min(list_readable, key=lambda x:(x["score"], x["name"]))
        
    print(f"Student name: {top_student['name']} -> Top Score: {top_student['score']}")
    print(f"Student name: {lowest_student['name']} -> Top Score: {lowest_student['score']}")

    # average score
    avg_student = sum(float(s['score']) for s in list_readable) / len(list_readable)
    print(f"Average Score:  {avg_student:.2f}")

        
        
        

        
        
   




    
        
        
    
    
    
    
        
        
        

