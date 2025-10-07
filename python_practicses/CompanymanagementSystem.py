# Base Class: Person

# Private attributes:

# __name

# __age

# Methods:

# __init__(self, name, age)

# get_name(), get_age()

# person_info() → prints:
# "Name: <name>, Age: <age>"

# 💼 Child Class: Employee (inherits from Person)

# Private attributes:

# __salary

# __position

# Methods:

# __init__(self, name, age, salary, position)

# get_salary()

# set_salary(new_salary) → only accepts positive values

# employee_info() → overrides person_info() and prints:
# "Employee: <name>, Age: <age>, Position: <position>, Salary: <salary>"

# 👨‍💻 Child Class: Developer (inherits from Employee)

# Private attribute:

# __language

# Methods:

# __init__(self, name, age, salary, position, language)

# employee_info() → overrides parent version to include programming language

# 👩‍💼 Child Class: Manager (inherits from Employee)

# Private attribute:

# __team → a list of Employee objects (composition)

# Methods:

# __init__(self, name, age, salary, position)

# add_team_member(employee) → adds an Employee to the team

# show_team() → prints info for all team members

# employee_info() → overrides parent method to include total team size

# 🏢 Class: Company

# Private attributes:

# __name

# __employees → list of Employee objects

# Methods:

# __init__(self, name)

# add_employee(employee) → adds an Employee (Developer, Manager, etc.)

# show_all_employees() → loops through all and calls employee_info()

# total_employees() → prints total employee count

class Person:
    def __init__(self,name,age):
       self.__name = name
       self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def person_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

class Employee(Person):
    def __init__(self, name, age,salary,position):
        super().__init__(name, age)
        self.__salary = salary
        self.__position = position
    def get_salary(self):
        return self.__salary
    def set_salary(self, new_salary):
        if new_salary >=0:
            self.__salary = new_salary
        else:
            print("Please enter 0 or a positive value")
    def employee_info(self):
        super().person_info()
        print(f"Position: {self.__position}, Salary: {self.__salary}")

class Developer(Employee):
    def __init__(self, name, age, salary, position,language):
        super().__init__(name, age, salary, position)
        self.__language = language
    def developer_info(self):
        super().employee_info()
        print(f"Programming Language: {self.__language}")

class Manager(Employee):
    def __init__(self, name, age, salary, position):
        super().__init__(name, age, salary, position)
        self.__team = []
        
    def add_member(self, new_member):
        self.__team.append(new_member)
    def show_team(self):
        print(f"Team member under{self.get_name()}")
        for team in self.__team:
            team.employee_info()
    def employee_info(self):
         super().employee_info()
         print(f"Team: {len(self.__team)}")

class Company:
    def __init__(self, name):
       self.__name = name
       self.__employees = []
    
    def add_employee(self, new_employee):
        self.__employees.append(new_employee)
    def all_employees(self):
        print(f"\nCompany: {self.__name}")
        for employee in self.__employees:
            employee.employee_info()
    def total_employees(self):
        print(f"Total Employees: {len(self.__employees)}")
    
company_name = Company("Technova LTD")
manager = Manager("Alice", 35,120000,"Project Manager")
developer1 = Developer("Bob", 28, 85000, "Developer","Python")
developer2 = Developer("Clara", 26, 80000, "Developer","Javascript")

manager.add_member(developer1)
manager.add_member(developer2)

company_name.add_employee(manager)
company_name.add_employee(developer1)
company_name.add_employee(developer2)

company_name.all_employees()
company_name.total_employees()
manager.employee_info()




    