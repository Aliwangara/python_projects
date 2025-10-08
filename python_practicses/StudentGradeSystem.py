# Class: Student

# Private Attributes:

# __name

# __score

# Class Attribute:

# __school_name = "Greenwood High"

# 🧠 Methods:

# __init__(self, name, score)
# → Initializes the student name and score.

# get_name(self)
# → Returns the student’s name.

# get_score(self)
# → Returns the student’s score.

# student_info(self)
# → Prints:
# "Student: <name>, Score: <score>, School: <school_name>"

# @classmethod change_school(cls, new_school)
# → Changes the school name for all students.

# @staticmethod is_valid_score(score)
# → Returns True if score is between 0 and 100, else False.

# 🧮 Program Flow

# Create three students:

# s1 = Student("Alice", 88)
# s2 = Student("Brian", 72)
# s3 = Student("Clara", 95)


# Check if a given score is valid using:

# print(Student.is_valid_score(110))


# Display all students’ info.

# Change the school name using:

# Student.change_school("Sunrise Academy")


# Display all students’ info again to confirm the school name changed.


class Student:
    __school_name = "Greenwood High"
    def get_school_name(self):
        return self.__school_name
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def student_info(self):
        print(f"Student: {self.get_name()} , Score: {self.get_score()}, School: {self.get_school_name()}")
    @classmethod
    def change_school(cls,new_school):
        cls.__school_name = new_school
    @staticmethod
    def is_valid_score(score):
        return score > 0 and score <=100
    

s1 = Student("Alice", 88)
s2 = Student("Brian", 72)
s3 = Student("Clara", 95)

print("student:", Student.is_valid_score(110))

all_students = [s1,s2,s3]

for s in all_students:
    s.student_info()
    print()
    print("-"*40)

Student.change_school("Sunrise Academy")

print("\nAfter School Change")
print()

for s in all_students:
    s.student_info()
    print()
    print("-"*40)


        
