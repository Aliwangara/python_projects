# Create a program that does the following:

# Opens a file called “journal.txt” in write mode.

# Writes 3 lines describing what you’ve learned in Python so far.

# Closes the file.

# Opens the same file in read mode.

# Reads the content and prints it to the console
# file_name = "journal.txt"

# with open(file_name,"w") as f:
#     f.write(f"Variables\nOOP\nData structures")
    
# with open(file_name, "r") as f:
#    content =  f.read()
#    print(content)



# Create a file named students.txt and:

# Write 3 student names (each on a new line).

# Read all lines using readlines().

# Print them one by one with line numbers.

# students_file = "students.txt"

# with open(students_file, "w") as f:
#     f.write("ali\n George\n Wangara")

# with open(students_file,"r") as f:
#     for i, line in enumerate(f,1):
#         print(f"{i}. {line.strip()}")

# Exercise: Student Progress Tracker
# Task:

# Create a Python program that:

# Writes the first batch of student names to a file using "w" mode.

# Appends new students to the same file using "a" mode.

# Reads all student names using "r" mode and prints them one by one.

students_file = "student.txt"

# with open(students_file,"w") as f:
#     f.write("Ali\nWangara\n")
 
# with open(students_file,'a') as f:
#     f.write("George")

# with open(students_file, 'r') as f:
#     for i,line in enumerate(f,1):
#         print(f"{i}. {line.strip()}")

# Ask the user how many new students to add.

# For each, ask for their name.

# Append all names to the file.

# Finally, read and print the updated, numbered list.

student_number = int(input("Enter number of the Students you want to add:   "))

for s in range(student_number):
    student_name = input("Enter name of the student:    ").lower()
    with open(students_file, 'a') as f:
        f.write(f"{student_name}\n")

with open(students_file, 'r') as f:
    for i, line in enumerate(f,1):
        print(f"{i}. {line.strip().title()}")




