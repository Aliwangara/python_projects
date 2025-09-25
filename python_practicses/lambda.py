
students = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 92},
    {"name": "John", "score": 75},
    {"name": "Mary", "score": 60},
    {"name": "Adam", "score": 75}
]


# sorting = sorted(students, key=lambda s:s["score"])
# sorting_name= sorted(students, key=lambda s:s["name"])
# print(sorting)
# print(sorting_name)
# lowest_score = min(students, key=lambda x:x['score'])
# print(lowest_score)


#  Challenge Task:

# You have this list:

numbers = [12, 7, 25, 18, 30, 5, 42, 19]


# Sort the numbers by remainder when divided by 5
# (use n % 5 inside the lambda).

sorting_numbers = sorted(numbers, key=lambda n:n%5)
print(sorting_numbers)


# Sort students by score, then by name if scores are equal
# (hint: return a tuple (score, name) in the lambda).

sort_by_score_then_name = sorted(students, key=lambda s:(s["score"],s["name"]))
print(sort_by_score_then_name)


# Sort by last letter
# You have:

words = ["apple", "banana", "grape", "kiwi", "mango"]


# 👉 Sort them by their last letter using sorted + lambda.


sort_by_last_letter = sorted(words , key=lambda l:l[-1])
print(sort_by_last_letter)

# Find the longest name

names = ["Ali", "Jennifer", "Chris", "Mo", "Elizabeth"]


# Use max(..., key=lambda ...) to get the longest name.

longest_name = max(names, key=lambda n:len(n))
print(longest_name)


students_list = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 92},
    {"name": "John", "score": 92},
    {"name": "Mary", "score": 60},
    {"name": "Adam", "score": 85}
]
#  Sort students by score (highest first), and if scores are equal, then by name (A–Z).

sort_score_name = sorted(students_list, key=lambda s:(s["score"],s["name"]))

print(sort_score_name)


# Absolute value sorting

abs_numbers = [-10, -2, 5, -7, 8, -1]


# 👉 Sort numbers by their absolute value using lambda.

absolute_sorting = sorted(abs_numbers, key=lambda a:abs(a))
print(absolute_sorting)



# Find closest to 10

nums = [3, 7, 11, 15, 9]


#  Use min(..., key=lambda ...) to find which number is closest to 10.
value = 10
closest_to_ten = min(nums, key=lambda c:abs(value -c))

print(closest_to_ten)





