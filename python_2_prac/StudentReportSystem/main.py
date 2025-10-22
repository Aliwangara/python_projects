# Create a class called Student with:

# Attributes: name, age, and marks (list of 3 subject marks).

# A method display_info() that prints the student’s full information, including average and grade.

import student_utils

class Student:
    def __init__(self, name,age,marks):
        self.__name = name
        self.__age = age
        self.__marks = list(marks)
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_marks(self):
        return self.__marks
    def display_info(self):
        print(f"Name: {self.get_name()}.\nAge: {self.get_age()}.\nMarks: {self.get_marks()}")

        average = student_utils.calculate_average(self.__marks)    
        grade = student_utils.get_grade(average)

        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
def add_student():
        name = input("Enter student's name: ")
        age = int(input(f"Enter {name}'s age: "))

        marks = []
        for i in range(4):
            mark = float(input(f"Enter mark {i} for {name}: "))
            marks.append(mark)

        student = Student(name, age, marks)
        return student



students = []

while True:
    print("\n=== Student Management System ===")
    print("1. Add new student")
    print("2. View all students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_student = add_student()
        students.append(new_student)
        print(f"\n✅ {new_student.get_name()} added successfully!")

    elif choice == "2":
        if not students:
            print("\nNo students found!")
        else:
            print("\n--- Student List ---")
            for student in students:
                student.display_info()

    elif choice == "3":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    
    
    
  


        

        

    