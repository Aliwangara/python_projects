# Class: Employee
# Private Attributes:

# __name

# __salary

# Methods:

# __init__(self, name, salary)

# get_name()

# get_salary()

# employee_info() → prints name and salary

# @abstractmethod calculate_bonus() → must be implemented by all subclasses

# Subclasses:

# Manager

# Bonus = 20% of salary

# Developer

# Bonus = 10% of salary

# Intern

# Bonus = fixed KES 5,000

# Program Flow:

# Create a list of employees:
# Manager("Ali", 120000), Developer("Sara", 90000), Intern("Brian", 30000)

# Loop through them:

# Show employee_info()

# Print Bonus: X

# Print total (salary + bonus)

# 🧠 Exercise 2: Abstract Class — Shape Area Calculator

# Abstract Base Class: Shape
# Abstract Method: area()
# Common Method: shape_info() → prints the type of shape

# Subclasses:

# Circle(radius)

# Rectangle(length, width)

# Triangle(base, height)

# Each subclass must:

# Implement area()

# Override shape_info() to show dimensions

# Program Flow:

# Create 1 object of each subclass

# Store in a list

# Loop to display each shape’s info and area.

# 🧠 Exercise 3: Abstract Class — Online Course Platform

# Abstract Base Class: Course
# Private Attributes:

# __title

# __duration (in hours)

# Methods:

# __init__(title, duration)

# get_title(), get_duration()

# course_info() → prints basic details

# @abstractmethod calculate_fee()

# Subclasses:

# ProgrammingCourse — rate = 500 per hour

# DesignCourse — rate = 400 per hour

# MarketingCourse — rate = 300 per hour

# Program Flow:

# Create objects:

# ProgrammingCourse("Python Basics", 30)

# DesignCourse("UI/UX Design", 25)

# MarketingCourse("Digital Ads", 20)

# Loop and:

# Display info

# Print total fee



from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
    def get_name(self):
        return self.__name
    def get_salary(self):
        return self.__salary
    def employee_info(self):
        print(f"Name: {self.get_name()}, Salary: {self.get_salary()}")

    @abstractmethod
    def calculate_bonus(self,new_bonus):
        pass

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def calculate_bonus(self,new_bonus):
        super().calculate_bonus(new_bonus)
        bonus = self.get_salary() * new_bonus
        return bonus
    def employee_info(self):
        super().employee_info() 

class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self, new_bonus):
        bonus = self.get_salary() * new_bonus
        return bonus

class Intern(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def calculate_bonus(self, new_bonus):
        bonus = new_bonus
        return bonus

manager = Manager("Ali", 120000)
dev = Developer("Sara", 90000)
new_intern = Intern("Brian", 30000)

employees = [manager, dev, new_intern]

# Display info and calculate bonuses
for emp in employees:
    emp.employee_info()
    bonus = emp.calculate_bonus(0.1 if not isinstance(emp, Intern) else 5000)
    print(f"Bonus: {bonus}\n{'-'*40}")



    
