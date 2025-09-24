# Write a program that calculates the sum of all even numbers from 1 → 50.
# 👉 Hint: use if i % 2 == 0 or range(2, 51, 2)

number = 0

for i in range(number,51):
    if i %2 == 0:
        number += i 
    print(number)

# Ask the user for a number n.
# Calculate the factorial (n! = n × (n-1) × … × 1).
# Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

# n  = int(input("Enter a number to calculate:   "))




# 3. Sum of digits

# Ask the user for a number (e.g., 1234).
# Calculate the sum of its digits (1 + 2 + 3 + 4 = 10).
# (Hint: use str(number) to loop through digits, then convert back to int).


num = (input("Enter a number eg:(1234):  "))

total_sum = 0

for i, number in enumerate(num):
  total_sum += int(number)
  if i < len(num) -1 :
    print(f"{number} +", end=" ")
  else:
     print(f"{number}", end=" ")
 
print(f"= {total_sum}")



