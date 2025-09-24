
# Level 1: Basic Functions

# Write a function greet() that prints "Hello, welcome to Python!". Call it.

# Write a function add_numbers(a, b) that returns the sum of two numbers.

# Write a function square(n) that returns the square of a number.

# def greet():
#     print( "Hello, welcome to Python!")
# greet()

# def add_numbers(a,b):
#     return print(a +b)

# add_numbers(10,20)

# def square(n):
#     return print(n**n)
# square(5)



# Level 2: With Conditions

# Write a function is_even(n) that returns True if a number is even, otherwise False.

# Write a function grade_checker(score) that returns the grade (A, B, C, Fail) using the rules you already know.

# Write a function max_of_three(a, b, c) that returns the largest of three numbers.

# def is_even(num):
#     if num %2==0:
#         return print("Even")
#     else:
#         return print("Odd")

# is_even(5)

# def grade_checker(grade):
#     if grade >=80:
#         return print("A")
#     elif grade >=70 and grade <= 79:
#         return print("B")
#     elif grade >=60 and grade <= 69:
#         return print("B")
#     else:
#         return print("Fail")
# grade_checker(70)

# def max_of_three(a,b,c):
#     return print(max(a,b,c))
# max_of_three(10,20,30)

# Level 3: Loops in Functions

# Write a function factorial(n) that returns the factorial of n.

# Write a function sum_of_digits(n) that returns the sum of digits of n.

# Write a function multiplication_table(n) that prints the multiplication table of n.

# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *=i
#     print(fact)
# factorial(5)



# def sum_of_digits(n = input("Enter a number: ")):
#     new_num = 0
#     for num in n:
#         new_num+=int(num)
#     print(new_num)
        
# sum_of_digits()

def multiplication_table(n = input("Enter a number: ")):
    for i in range(1,11):
         new = int(n)
         new*=i
         print(new)
multiplication_table()





