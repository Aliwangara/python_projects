from StudentInfomanager import main_file
import os
import json



students_file = "students.json"

student_data = main_file.student_data()

if not os.path.exists(students_file):
    with open(students_file,"r") as f:
        try:
         reader = json.load(f)
        except FileNotFoundError as e:
           print(e)
        else:
           print(json.dumps(reader, indent=4))

       


with open(students_file,"w")as f:
    json.dump(student_data,f,indent=4)

with open(students_file, 'r') as f:
    reader = json.load(f)
    print(reader)
    


