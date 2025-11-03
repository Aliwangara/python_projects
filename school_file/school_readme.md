<!-- Project: Student Grade Management System
🎯 Goal

Create a program that:

Manages student data (name, ID, and scores)

Calculates their average and grade

Stores the data in a text file

Reads back and displays all students neatly

🪜 Step-by-Step Tasks
1. Create a Student class

Each student should have:

student_id

name

scores (a list of integers)

Include methods:

calculate_average()

get_grade() → use these rules:

A: 80–100
B: 70–79
C: 60–69
D: 50–59
F: below 50

2. Add user input

Ask the user to:

Enter student ID

Enter name

Enter 3 scores (store them in a list)

3. Store the student info

After creating a student, write their:
ID, Name, Average, Grade
into a file named "AQQ2".

4. Read and display

When the user is done adding students, open students.txt and display all saved records like this:

ID       Name          Average   Grade
--------------------------------------
S001     Alice          87.5       A
S002     Bob            64.3       C

5. Bonus (if you want a challenge)

Add menu options:

1. Add new student
2. View all students
3. Search student by ID
4. Exit -->