from StudentInfomanager import main_file
import os
import json


students_file = "students.json"

student_data = main_file.student_data()

# if not os.path.exists(students_file):
#     with open(students_file,"r") as f:
#         try:
#             existing_data = json.load(f)
#         except json.JSONDecodeError:
#             existing_data = []
# else:
#     existing_data = []

# existing_data.extend(student_data)


# with open(students_file,"w")as f:
#     json.dump(student_data,f,indent=4)

with open(students_file, 'r') as f:
    reader = json.load(f)
    print(reader)
    


