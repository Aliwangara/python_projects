# Build a small program that:

# Registers students.

# Validates their age and marks.

# Uses custom exceptions and proper try/except handling.

# 🧠 Requirements
# 1️⃣ Create Two Custom Exception Classes:
# InvalidAgeError(Exception)
# InvalidMarkError(Exception)

# 2️⃣ Create a Function:
# def register_student(name, age, marks)


# Inside this function:

# If age < 18, raise InvalidAgeError("Student must be 18 or older")

# If any mark in marks is less than 0 or greater than 100, raise InvalidMarkError("Marks must be between 0 and 100")

# Otherwise, print "✅ Registration successful!" and display name, age, average marks, and grade.

# 🧮 Grade Rules:
# Average	Grade
# 80–100	A
# 70–79	B
# 60–69	C
# 50–59	D
# <50	E
# 🧱 Program Flow (Main Script)

# Use a while True loop to allow multiple registrations.

# Ask for:

# Enter name:
# Enter age:
# Enter marks separated by space:


# Convert marks into a list of floats.

# Call register_student().

# Handle exceptions with user-friendly messages.

# Ask if they want to register another student (y/n).

# 💻 Example Output

# Case 1 – Invalid Age

# Enter name: Ali
# Enter age: 16
# Enter marks separated by space: 70 80 90
# ⚠️ Error: Student must be 18 or older


# Case 2 – Invalid Marks

# Enter name: Fatma
# Enter age: 19
# Enter marks separated by space: 70 105 80
# ⚠️ Error: Marks must be between 0 and 100


# Case 3 – Success

# Enter name: Mariam
# Enter age: 20
# Enter marks separated by space: 80 75 90
# ✅ Registration successful!
# Name: Mariam
# Age: 20
# Average: 81.67
# Grade: A

class InvalidAgeError(Exception):
    pass
class InvalidMarksError(Exception):
    pass

def register_student(name,age,marks):
    if age < 18:
        raise InvalidAgeError("Student must be 18 or older")
    else:
        print("Valid Age")
    
    
    average = sum(marks)/ len(marks)
    
    if any(0< m or m> 100 for m in marks):
        raise InvalidMarksError("Marks must be between 0 and 100")
    else:
        print("Valid marks")

    if average >= 80 :
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average>= 50 :
        grade = "D" 
    else:
        grade = "E"

    print("✅ Registration successful!")
    print(f"Name: {name.capitalize()}\nAge: {age}\nAverage: {average:.2f}\nGrade: {grade}")
 
while True:
    try:
        
        name = input("Enter name:   ").lower()
        age = int(input("Enter Age:  "))
        marks_input = input("Enter marks separated by space: ")

        marks = [float(m) for m in marks_input.split()]
        


        register_student(name,age,marks)
    
    except InvalidAgeError as e:
        print("Error",e)
    except InvalidMarksError as e:
        print("Error",e)
    except ValueError:
        print("⚠️ Error: Please enter valid numbers for age and marks.")
    else:
        print("Valid credentials")
    finally:
        print("Thank You")
    
    new_student_input = input("You want to add new student (y or n):  ").lower()

    if new_student_input != 'y':
        print("Exiting system. Goodbye!")
        break