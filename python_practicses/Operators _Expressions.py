# Math practice

# Ask the user for two numbers.

# Print their sum, difference, product, quotient, remainder, and power.

# first_number = float(input("Enter first number:  "))
# second_number = float(input("Enter second number:  "))

# print(f"The sum of {first_number} + {second_number} = {first_number  + second_number:.2f}")
# print(f"The difference of {first_number} - {second_number} = {first_number  - second_number:.2f}")
# print(f"The product of {first_number} * {second_number} = {first_number  * second_number:.2f}")
# print(f"The quotient of {first_number} / {second_number} = {first_number  / second_number:.2f}")
# print(f"The remainder of {first_number} % {second_number} = {first_number  % second_number:.2f}")
# print(f"The power of {first_number} ** {second_number} = {first_number  ** second_number:.2f}")

# Ask for a number.

# Print whether it’s greater than 10, equal to 10, or less than 10.

# number = float(input("Enter a number to confirm if it's less than of greater than 10: "))

# if number > 10:
#     print(f"{number} is greater than 10")
# elif number < 10:
#     print(f"{number} is less than 10")
# else:
#     print("Correct")


# Logical practice

# Ask the user for age and whether they have an ID (True/False).

# Print if they are allowed to enter a club (must be ≥18 and have ID).

# age = int(input("Enter Your Age:  "))
# have_id = input("Have an Id (True or False):   ").capitalize()

# if age >= 18 and have_id == "True":
#     print("Allowed to enter the Club")
# else:
#     print("You aren't allowed in the club")


# 📝 Micro follow-up task before moving on

# Take your Math Practice script and extend it:

# Ask the user for three numbers instead of two.

# Print the largest and smallest number using comparison operators (>, <).

first_number = float(input("Enter first number:  "))
second_number = float(input("Enter second number:  "))
third_number = float(input("Enter third number:  "))

if first_number >= second_number and first_number >= third_number:
    greatest = first_number
elif second_number >= first_number and second_number >= third_number:
    greatest = second_number
else:
    greatest = third_number 

if first_number <= second_number and first_number <= third_number:
    smallest = first_number
elif second_number <= first_number and second_number <= third_number:
    smallest = second_number
else:
    smallest = third_number

print(f"Smallest number is {smallest}")
print(f"Largest number is {greatest}")




