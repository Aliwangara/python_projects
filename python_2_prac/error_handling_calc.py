# Goal

# Build a calculator that:

# Accepts two numbers (int or float).

# Accepts an operation: +, -, *, /.

# Performs the calculation and displays the result.

# Uses try/except to handle all possible errors.

# Logs any errors to a file named error_log.txt.

# Keeps running until the user types "exit".

# ⚙️ Requirements 

# Handle these errors gracefully:

# Invalid numeric input → ValueError

# Division by zero → ZeroDivisionError

# Invalid operation → custom exception or message

# Log errors (append mode) like this:

error_file = "error_log.txt"

try:
    num1 = float(input("Enter first numbe:   "))
    num2 = float(input("Enter second number:   "))
    operation = input("Enter values(+,-,/,*):   ")
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '*':
        result = num1 * num2
    else:
        result = "Operations Error"
        with open(error_file, 'a', newline="") as f:
            f.write(result)
except ZeroDivisionError:
    print("Cant be divided by zero")
    with open(error_file, 'a', newline="") as f:
            f.write("Cant be divided by zero")
except ValueError:
    print("Value Error")
    with open(error_file,'a',newline="") as f:
        f.write("Value Error")
else:
    print(f"Result: {result:.2f}")
finally:
    print("Thank you for using our calculator")
