# Write a script that asks for first and last name and prints them joined and the total characters in the full name.


# first_name = input("Enter Your first Name: ")
# last_name = input("Enter Your last Name: ")

# full_name= first_name + last_name

# print(f"Your name is {full_name} with a total of {len(full_name)} characters")

# Make a small “profile” dictionary: { 'name': ..., 'age': ..., 'languages': [...] } — 
# then print languages[0] and the type() of the profile.

# profile = {
#     "name": "Ali wangara",
#     "age": 21,
#     "languages": ["english", "Luhya", "Kiswahili"]
# }

# print(f"{profile['languages']} {type(profile)}")



# Make a tiny CLI that asks the user for three expenses (as floats), 
# stores them in a list, prints total and average (use sum() and len()).

first_expense = float(input("Enter First expense: "))
second_expense = float(input("Enter second expense: "))
third_expense = float(input("Enter third expense: "))

expense_list = []

expense_list.append(first_expense)
expense_list.append(second_expense)
expense_list.append(third_expense)

total = sum(expense_list)
length = len(expense_list)
print(f"{total/length:.2f}")

