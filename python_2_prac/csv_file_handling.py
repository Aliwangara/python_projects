import csv

# student_file = "students.csv"

# with open(student_file, 'w',newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Name", "Age", "Score"])
#     writer.writerow(["Ali", 20, 85])
#     writer.writerow(["George", 22, 90])
#     writer.writerow(["Wangara", 19, 78])

# with open(student_file, 'r') as f:
#     reader = csv.reader(f)
#     next(reader)
#     for name,age,score in reader:
#         print(f"{name} is {age} years old and scored {score}.") 



# Creates a CSV file students.csv.

# Writes the header (Name, Age, Score) and 3 student records.

# Reads the file, skipping the first line (header).

# Prints a neat summary for each student.

students_csv = "students.csv"

with open(students_csv,'a',newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Age","Score"])
    writer.writerow(["Ali",21,50])
    writer.writerow(["george",21,70])
    writer.writerow(["Wangara",22,80])
    
with open(students_csv,"r") as f:
    reader = csv.reader(f)
    next(reader)
    for name,age,score in reader:
        print(f"{name} is {age} years old and scored {score}.") 

