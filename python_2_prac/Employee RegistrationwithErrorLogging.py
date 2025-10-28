
class EmptyFieldError(Exception):
    pass
class InvalidSalaryError(Exception):
    pass
class InvalidAgeError(Exception):
    pass

error_file = "error_log.txt"
employee_file = "employees.txt"
def register_employee(name, age, salary, department):
    if name and department == "":
     raise EmptyFieldError("Name and Department cannot be empty")
    else:
       print("Valid Input")
    
    if age < 18  or age > 65:
       raise InvalidAgeError("Age must be between 18 and 65") 
    else:
       print("Valid age")
    if salary < 15000:
       raise InvalidSalaryError("Salary must be at least 15000")
    else:
       print("valid salary")
    print("✅ Successfully registered employee")
    print(f"Name: {name.capitalize()} | Age: {age} | Salary: {salary} | Department: {department}")

while True:
    try:
        name = input("Enter name: ").lower()
        age = int(input("Enter age: "))
        salary = float(input("Enter Salary: "))
        department = input("Enter Department:  ").upper()

        register_employee(name,age,salary,department)

        with open(employee_file,'a',newline="") as f:
           f.write(f"Name: {name}, Age: {age}, Salary: {salary:,}, Department: {department}")

    except EmptyFieldError as e:
       print("Error logged to error_log.txt")
       with open(error_file,'a',newline="") as f:
          f.write(f"Error: {e}")
    except InvalidAgeError as e:
       print("Error logged to error_log.txt")
       with open(error_file,'a',newline="") as f:
          f.write(f"ERROR: {e}")
    except InvalidSalaryError as e:
       print("Error logged to error_log.txt")
       with open(error_file, 'a',newline="") as f:
          f.write(f"ERROR: {e}")
    except ValueError:
       print("Enter a valid age and salary")
    else:
       print("Data saved to employees.txt")
    finally:
       print("Thank You.")

    new_employee = input("Do you want to add a new employee(y or n): ").lower()

    if new_employee != 'y':
       print("Thank you!")
       break




