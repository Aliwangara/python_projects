# Class: Employee

# Private Attributes:

# __name

# __position

# __salary

# Class Attributes:

# __company_name = "TechVision Ltd"

# __employee_count = 0

# 🧠 Methods:
# __init__(self, name, position, salary)

# Initializes the employee details.

# Increases the total employee count by 1 every time a new employee is created.

# get_name(self)

# Returns the employee’s name.

# get_salary(self)

# Returns the employee’s salary.

# employee_info(self)

# Prints:

# Employee: <name>, Position: <position>, Salary: $<salary>, Company: <company_name>

# @classmethod change_company(cls, new_name)

# Changes the company name for all employees.

# @classmethod total_employees(cls)

# Prints:

# Total employees: <employee_count>

# @staticmethod is_valid_salary(salary)

# Returns True if salary > 0, otherwise False.

# 🧮 Program Flow

# Create three employees:

# e1 = Employee("Alice", "Manager", 120000)
# e2 = Employee("Brian", "Developer", 95000)
# e3 = Employee("Clara", "Intern", 40000)


# Check if -5000 is a valid salary using:

# print(Employee.is_valid_salary(-5000))


# Display each employee’s info.

# Print total employees using:

# Employee.total_employees()


# Change the company name using:

# Employee.change_company("NextGen Tech")


# Display all employees’ info again to confirm the company name changed.



class Employee:
    __company_name = "TechVision Ltd"
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
    def employee_info(self):
        print(f"Employee: {self.get_name()}, Position: {self.get_position()}, Salary: ${self.get_salary()}, Company: {Employee.__company_name}")
    @classmethod
    def change_company(cls,new_name):
        cls.__company_name = new_name
    @classmethod
    def total_employees(cls):
        print(f"Total employees: {cls.__employee_count}")
    @staticmethod
    def is_valid_salary(salary):
        return salary >0

    
e1 = Employee("Alice", "Manager", 120000)
e2 = Employee("Brian", "Developer", 95000)
e3 = Employee("Clara", "Intern", 40000)


print("Employee Valid: ", Employee.is_valid_salary(-5000))

employees = [e1,e2,e3]

for employee in employees:
    employee.employee_info()
    print("-"*40)
employee.total_employees()

Employee.change_company("NextGen Tech")


print("\nEmployees after Change")

for employee in employees:
    employee.employee_info()
    print("-"*40)



