# CONCEPT: Handling Exceptions with try and except

# To stop a crash, you handle the exception gracefully using try and except.

# 🧩 Syntax
# try:
#     # Code that might cause an error
# except SomeError:
#     # What to do if that error happens

# ✅ Example
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("You can’t divide by zero!")


# 🖥️ Output:

# You can’t divide by zero!


# The program no longer crashes — it handles the error politely 😎

# 🧠 3️⃣ Handling Multiple Error Types

# Sometimes you want to handle different errors differently.

# Example
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("Please enter a valid number.")
# except ZeroDivisionError:
#     print("Number cannot be zero.")


# 🧾 Possible Outputs:

# Enter a number: abc
# Please enter a valid number.

# Enter a number: 0
# Number cannot be zero.

# 🧠 4️⃣ The else and finally Blocks
# 🔹 else: runs if no error occurs
# 🔹 finally: runs always, whether error or not
# Example
# try:
#     num = int(input("Enter number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# else:
#     print("Success! Result:", result)
# finally:
#     print("Program complete.")


# 🧾 Output (when user enters 2):

# Success! Result: 5.0
# Program complete.


# 🧾 Output (when user enters 0):

# Cannot divide by zero.
# Program complete.

# 5️⃣ Catching All Errors (Not Recommended but Useful Sometimes)
# try:
#     name = undefined_var
# except Exception as e:
#     print("An error occurred:", e)

# Create a program that asks for two numbers and divides them.
# Handle:

# Division by zero

# Invalid input

# 2️⃣ Add a finally block that prints:
# "Thanks for using our calculator!"


try:
    num = int(input("Enter a number:   "))
    result = 10/num
except ZeroDivisionError:
    print("Number cannot be zero")
except ValueError:
    print("Please enter a valid number")
else:
    print(f"Result: {result}")
finally:
    print("Thanks for using our calculator!")
