# Class Employee

# Private attributes: __name, __position, __salary

# Class attributes: __company_name = "TechWorks" and __employee_count = 0

# Methods:

# __init__() → initialize employee info and increase count

# get_salary()

# employee_info() → display details

# @classmethod total_employees()

# @classmethod change_company()

# @staticmethod is_valid_salary()

# Subclass Manager(Employee)

# Add bonus attribute

# Override employee_info() to include bonus

# In main program:

# Create 3 employees and 1 manager

# Display their info

# Change company name and display again

# Show total employees


class Employee:
    __company_name = "TechWorks"
    __employee_count = 0
    def __init__(self,name,position,salary):
        
        self.__name = name
        self.__position = position
        self.__salary = salary
        Employee.__employee_count +=1
    def get_name(self):
        return self.__name
    def get_position(self):
        return self.__position
    def get_salary(self):
        return self.__salary
    def employment_info(self):
        print(f"Name:{self.get_name()}, Position: {self.get_position()}, Salary: {self.get_salary()}, Company: {Employee.__company_name}")
    @classmethod
    def total_employees(cls):
        print(f"Total Employees: {cls.__employee_count}")
    @classmethod
    def change_company(cls, new_name):
        cls.__company_name = new_name
    @staticmethod
    def is_valid_salary(salary):
        return salary >0
    
class Manager(Employee):
    def __init__(self, name, position, salary,bonus):
        super().__init__(name, position, salary)
        self.__bonus = bonus
    
    def employment_info(self):
        super().employment_info()
        print(f"Bonus: {self.__bonus}")

emp1 = Employee("Ali", "Dev", 20000)
emp2 = Employee("George", "Dev", 40000)
emp3 = Employee("Wangara", "Dev", 70000)

man = Manager("AliG", "manager",20000,5000)

company_info = [emp1,emp2,emp3,man]

for employee in company_info:
    employee.employment_info()
    print("-"*40)

Employee.change_company("GikTek")

for employee in company_info:
    employee.employment_info()
    print("="*40)
Employee.total_employees()

print("Valid salary check (-500):", Employee.is_valid_salary(-500))
print("Valid salary check (20000):", Employee.is_valid_salary(20000))

