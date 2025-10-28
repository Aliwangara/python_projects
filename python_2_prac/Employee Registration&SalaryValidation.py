
class InvalidAgeError(Exception):
    pass

class InvalidSalaryError(Exception):
    pass

def register_employee(name,age,salary):

    if age < 18 or age > 65:
        raise InvalidAgeError("Age must be between 18 and 65")
    else:
        print("Welcome")
    
    if salary < 15000:
        raise InvalidSalaryError("Salary must be at least 15000")
    else:
        print("Salary above 15000")

    if salary >= 15000 and salary <= 29999:
        tax_category = "Low Tax"
    elif salary >= 30000 and salary <= 59999:
        tax_category = "Medium Tax"
    elif salary >= 60000:
        tax_category = "High Tax" 
    else:
       tax_category = "Please enter a valid salary" 
    print("✅ Registration successful!")
    print(f"Name: {name}\nAge: {age}\nSalary: {salary}\nTax Category: {tax_category}")


while True:
    try:
        name = input("Enter name:  ").lower()
        age = int(input("Enter Age:  "))
        salary = float(input("Enter Salary: "))

        register_employee(name,age,salary)
    except InvalidAgeError as e:
        print("⚠️", e)
    except InvalidSalaryError as e:
        print("Error", e)
    except ValueError:
        print("invalid input.Please enter a valid number for age and salary")
    else:
        print("🩷 Valid input. Welcome")
    finally:
        print("Thank you!")

    new_employee = input("Do you want to add a new employee(y or n):  ").lower()

    if new_employee !='y':
        print("Thank you")
        break



