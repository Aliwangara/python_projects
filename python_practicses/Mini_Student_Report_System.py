# Requirements:

# Ask for student details:

# Name

# Age

# Grade checker:

# Ask for a score (0–100).

# Assign a grade:

# ≥ 80 → A

# 70–79 → B

# 60–69 → C

# < 60 → Fail

# Number analysis:

# Ask for a number n.

# Print whether n is even or odd.

# Print the factorial of n.

# Print the sum of digits of n.

# Loop practice:

# Print the multiplication table of n (from 1 to 10).

# Summary report:
# At the end, print something like:

# --- Student Report ---
# Name: Ali
# Age: 21
# Grade: B
# Number chosen: 6
# Even/Odd: Even
# Factorial: 720
# Sum of digits: 6
# Multiplication table printed above
# ----------------------


name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
score = float(input("What is your score:  "))

if score >=80 and score<=100:
    result = "A"
elif score >=70 and score <=79:
    result = "B"
elif score >=60 and score <=69:
    result = "C"
else:
    result = "Fail"



n = input("Enter a Number:  ")

if int(n) %2 == 0:
   res = "ODD"
else:
    res = "EVEN"

factorial = 1

for i in range(1, int(n)+1):
    factorial *=i


total = 0
for i,  number in enumerate(n):
    total +=int(number)
    if i<len(n) -1:
        print(f"{number} +", end=" ")
    else:
        print(f"{number}", end=" ")



for num in range(1,11):
   n_multiple = int(n)
   n_multiple *= num
   print(n_multiple)
   


print("--- Student Report ---")
print(f"Name: {name}\nAge: {age}\nGrade: {result}\nNumber Chosen: {n}\nEven/Odd: {res}\nFactorial: {factorial}\nSum of digits {total}\nMultiplication table printed above")


