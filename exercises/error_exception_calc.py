# Build a small program that:

# Takes two numbers and an operation (+, -, *, /)

# Handles:

# Division by zero

# Invalid operation

# Non-numeric input

# Always prints a “Thank you” message in finally

try:
    num1  = float(input("Enter first number:   "))
    num2 = float(input("Enter second number:   "))
    operation = input("Enter operation(+,-,/,*):    ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result  = num1 * num2
    elif operation == '/':
       result =  num1 / num2
    else:
        raise ValueError("Invalid operation! Please use +, -, *, or /")
    
except ZeroDivisionError:
    print("Cant be divided by 0")
except  ValueError:
    print("Please enter a valid value")
except ValueError as e:
    print("⚠️",e)
else:
    print("Result:", result)
finally:
    print("Thank You!")

