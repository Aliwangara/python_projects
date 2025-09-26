# Assignment — Student Report System

# You’ll build a CLI program that manages students and their scores.

# Features to include:

# Add a student

# Ask for student’s name.

# Ask for 3 scores (integers).

# Store them in a dictionary like:

# {"Ali": [85, 90, 78]}


# View all students

# Print each student with their scores and their average.

# Search for a student

# Ask for a name.

# If found, show their scores + average.

# Top student

# Use max(..., key=lambda ...) to find the student with the highest average score.

# Sort students

# Option to sort students by:

# Name (A–Z)

# Average score (highest → lowest)

# Exit

students = []

def add_student():
    name = input("Enter name of the student:    ").lower()
    scores = input("Enter student scores eg:(85 90 78):    ")

    student_info = {
        "name":name,
        "score":list(map(int,scores.split()))
    }
    students.append(student_info)


add_student()

def view_all_students():
   for student in students:
    print(f"{student["name"]}'s scores are {student["score"]} with an average of {sum(student["score"]) / len(student["score"])}")
view_all_students()