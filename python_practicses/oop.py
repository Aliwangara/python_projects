

# class Student:
#     def __init__(self, name ,age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#     def average(self):
#         return sum(self.score)/ len(self.score)
    
#     def add_score(self, new_score):
#         self.score.append(new_score)

#     def __str__(self):
#         return f"{self.name} -> Age:{self.age} -> scores: {self.score} -> Average: {self.average():.2f}"
    
# students = []
# # Add students
# students.append(Student("Ali", 20, [85, 90, 78]))
# students.append(Student("Amina", 19, [92, 88, 84]))


# for s in students:
#     print(s)

# # Find top student
# top = max(students, key=lambda s: s.average())
# print("Top student:", top)
        

# OOP EXERCISE:

# Practice more with your Student class

# Add a method to update the student’s age

# Add a method to remove the last score

# Add a method to check if a student passed (average ≥ 60)

class Student:
    def __init__(self,name,age, score):
        self.name = name
        self.age = age
        self.score = score
    def 

