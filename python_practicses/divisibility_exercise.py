# Divisible by 3

# Ask the user for a number.
# 👉 Print "Divisible by 3" if the remainder is 0, otherwise "Not divisible by 3".

number_input = int(input("Enter a Number:  "))

# if number_input %3 ==0:
#     print("Divisible by 3")
# else:
#     print("Not divisible by 3")

# Ask the user for a number.
# 👉 If divisible by both 2 and 3, print "Yes". Else, print "No".

# if number_input %3 == 0  and number_input % 2:
#     print("Yes")
# else:
#     print("no")

# Remainder check

# Ask the user for two numbers: a and b.
# 👉 Print the remainder when a is divided by b.

# a = int(input("Enter a number:  "))
# b = int(input("Enter a number"))

# c= a % b


# if c == 0:
#     print(f"{a} is diviscible by {b}")
# else:
#     print(f"The remainder is {c}")


# Advanced: Leap Year (trickier 🧩)

# A year is a leap year if:

# divisible by 4,

# but not divisible by 100,

# unless it’s also divisible by 400.

# 👉 Write a script that asks for a year and prints whether it’s a leap year or not.


year = int(input("Enter year to check if it is a leap year:  "))

if year % 4 ==0 and year % 400 == 0:
    print('LEAP')
elif year % 100 != 0:
    print("Not leap")
else:
    print("not leap")


