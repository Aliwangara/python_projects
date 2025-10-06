

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

# class Car:
#     def __init__(self, name, make, yom):
#         self.name = name
#         self.make = make
#         self.yom = yom
#     def car_info(self):
#         print(f"Name: {self.name}")
#         print(f"Make: {self.make}")
#         print(f"Year of Model: {self.yom}")
#     def update_year(self, new_year):
#         self.yom = new_year

# # car1 = Car.car_info()
# car1 = Car("Toyota", "LC 200", 2023)
# car1.update_year(2024)
# car1.car_info()


# Exercise 2

# Exercise: Car Attribute Updater

# Modify your Car class:

# Add a method update_name() → to change car name.

# Add a method update_make() → to change the make.

# Add a method increase_year(by) → adds a number to current year.
# Example: if yom = 2020, and you call increase_year(3),
# it becomes 2023.

# Test all of them by printing before and after.


class Car:
    def __init__(self, name, make, yom):
        self.__name = name
        self.__make = make
        self.__yom = yom
    
    def car_info(self):
        print(f"Name: {self.__name}\nMake: {self.__make}\nYear of model: {self.__yom}")

    def update_yom(self,new_year):
        self.__yom = new_year
    def update_name(self, new_name):
        self.__name = new_name
    def increase_year(self, number):
        self.__yom += number
    def set_yom(self, new_yom):
        if new_yom > 2000:
            self.__yom = new_yom
        else:
            print("Invalid Year must be 2000 or newer ")

car1 = Car("Lexus", "LX 600", 1990)
car1.update_name("Toyota")
# car1.increase_year(2)
car1.car_info()


