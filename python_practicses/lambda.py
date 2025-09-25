
students = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 92},
    {"name": "John", "score": 75},
    {"name": "Mary", "score": 60}
]


sorting = sorted(students, key=lambda s:s["score"])
sorting_name= sorted(students, key=lambda s:s["name"])
print(sorting)
print(sorting_name)
lowest_score = min(students, key=lambda x:x['score'])
print(lowest_score)





