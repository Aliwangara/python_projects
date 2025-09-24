# Write a Python program that does the following:

# Ask the user for a number (let’s call it n).

# Print the sum of all even numbers from 1 → n.

# Example: if n = 10, sum = 2 + 4 + 6 + 8 + 10 = 30.

# Print the factorial of n.

# Example: if n = 5, factorial = 120.

# Print the sum of the digits of n.

# Example: if n = 123, sum = 1 + 2 + 3 = 6.

n = input("Enter a number:   ")
# factorial = 1

# for i in range(1, int(n)+1):
#     factorial *= i
# print(factorial)
total = 0
for i, number in enumerate(n):
    total += int(number)
    if i < len(n)-1:
      print(f"{number} +", end=" ")
    else:
       print(f"{number}", end=" ")
       
print(f" = {total}")
    

