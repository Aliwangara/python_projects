# Requirements
# 🧱 Base Class: Employee

# Private Attributes:

# __name

# __salary

# Methods:

# __init__(self, name, salary)

# get_name() → returns employee name

# get_salary() → returns salary

# set_salary(new_salary) → updates salary (must be > 0)

# calculate_bonus() → prints "Generic employee bonus: 5% of salary"

# employee_info() → prints "Employee: X, Salary: Y"

# 💻 Child Class: Developer (inherits from Employee)

# Additional Private Attribute:

# __programming_language

# Override Methods:

# calculate_bonus() → prints "Developer bonus: 10% of salary"

# employee_info() → include programming language

# 📊 Child Class: Manager (inherits from Employee)

# Additional Private Attribute:

# __team_size

# Override Methods:

# calculate_bonus() → prints "Manager bonus: 15% of salary"

# employee_info() → include team size

# Child Class: Designer (inherits from Employee)

# Additional Private Attribute:

# __design_tool

# Override Methods:

# calculate_bonus() → prints "Designer bonus: 8% of salary"

# employee_info() → include design tool



class Employee:
    def __init__(self, name,salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name
    def get_salary(self):
        return self.__salary
    def set_salary(self, new_salary):
        if new_salary > 0:
         self.__salary = new_salary
        else:
            print("New salary should be greater then 0")
    def calculate_bonus(self):
        print("Generic employee bonus: 5% of salary")
    def employee_info(self):
        print(f"Employee {self.__name}, Salary: {self.__salary}")

class Developer(Employee):
    def __init__(self, name, salary,programming_language):
        super().__init__(name, salary)
        self.__programming_language = programming_language
    def calculate_bonus(self):
        print("Developer bonus: 10% of salary")
    def employee_info(self):
        super().employee_info()
        print(f"Programming Language: {self.__programming_language}")

class Manager(Employee):
    def __init__(self, name, salary,team_size):
        super().__init__(name, salary)
        self.__team_size = team_size
    def calculate_bonus(self):
        print("Manager bonus: 15% of salary")
    def employee_info(self):
        super().employee_info()
        print(f"Team Size: {self.__team_size}")

class Designer(Employee):
    def __init__(self, name, salary,design_tool):
        super().__init__(name, salary)
        self.__design_tool = design_tool
    def calculate_bonus(self):
        print("Designer bonus: 8% of salary")
    def employee_info(self):
        super().employee_info()
        print(f"Design Tool: {self.__design_tool}")

employees = [
    Developer("Alice", 80000, "Python"),
    Manager("Bob", 120000, 8),
    Designer("Charlie", 70000, "Figma")
]

for emp in employees:
    emp.employee_info()
    emp.calculate_bonus()
    print("-" * 40)


    








