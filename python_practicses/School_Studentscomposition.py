# Requirements
# Class: Student

# Private Attributes:

# __name

# __grade

# Methods:

# __init__(self, name, grade)

# student_info(self) → prints "Student: <name>, Grade: <grade>"

# Class: School

# Private Attributes:

# __name

# __students → list of Student objects

# Methods:

# __init__(self, name) → initializes school name and empty student list

# add_student(self, student) → adds a Student object to the list

# show_students(self) → prints all students using each student’s student_info()

# total_students(self) → prints "Total students: X"

# 🧩 Program Flow

# Create a school named "Sunrise Academy".

# Create three students:

# "Alice", Grade 8

# "Brian", Grade 7

# "Clara", Grade 8

# Add the students to the school.

# Show all students.
# Show total number of students.

class Student:
    def __init__(self, name,grade):
        self.__name = name
        self.__grade = grade
    def get_name(self):
        return self.__name
    def get_grade(self):
        return self.__grade
    def student_info(self):
        print(f"Student: {self.__name} Grade: {self.__grade}")

class School:
    def __init__(self,name):
        self.__name = name
        self.__students = []
    def add_student(self, student):
        self.__students.append(student)
    def show_students(self):
        print(f"\nSchool: {self.__name}")
        for student in self.__students:
            student.student_info()
    def total_students(self):
        print(f"Total Students: {len(self.__students)}")

school_name = School("Sunrise Academy")
student1 = Student("alice", "grade8")
student2 = Student("Brian", "grade7")
student3 = Student("Clara", "grade8")

school_name.add_student(student1)
school_name.add_student(student2)
school_name.add_student(student3)

school_name.show_students()
school_name.total_students()






