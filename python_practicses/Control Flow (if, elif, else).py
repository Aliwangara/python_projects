# Grade Checker
# Ask the user for their score (0–100).

# ≥ 80 → "A"

# 70–79 → "B"

# 60–69 → "C"

# < 60 → "Fail"

# score = float(input("Enter the score of the user:   "))

# if score >= 80:
#     grade = "A"
# elif score >= 70 and score <= 79:
#     grade = "B"
# elif score >= 60 and score <= 69:
#     grade = "C"
# else:
#     grade = "Fail"

# print(f"Grade is {grade}")

# number = float(input("Enter number to check if its even or odd:    "))

# if number % 2 == 0:
#     result = "Even"
# else:
#     result = "Odd"

# print(f"{number} is {result}")


# Nested Conditions — ATM Example
# Ask the user for a PIN (e.g., 1234).

# If correct → ask withdrawal amount.

# If amount ≤ balance (say 1000) → allow withdrawal.

# Else → "Insufficient funds".

# If wrong PIN → "Access denied".
pin = 12345
user_pin = int(input("Enter account Pin:    "))

if user_pin ==pin:
    balance = 10000
    withdrawal_input = float(input("How much do you want to withdraw:  "))
    if withdrawal_input <= balance:
        print(f"You have withdrawn {withdrawal_input} your Account balance is {balance-withdrawal_input}")
    else:
        print(f"insufficient funds {withdrawal_input} your balance is {balance}")
else:
    print("Access denied")
