import json
import os

students_file = "students.json"

name = input("Enter name: ")
age = int(input("Enter age: "))
marks = []

print("=== Enter marks for 3 subjects ===")
for i in range(3):
    marks_input = float(input(f"Enter mark {i+1}: "))
    marks.append(marks_input)


student_records = {
    "name":name,
    "age": age,
    "marks": marks
}

students_list =[]

students_list.append(student_records)

with open(students_file, 'w') as f:
    json.dump(students_list,f,indent=4)
    f.write('\n')
    
if os.path.exists(students_file) == False:
        print("Folder doesn't exist ")
elif os.path.getsize(students_file) == 0:
        print("Student file is empty")
else:
        with open(students_file, "r") as f:
            data = json.load(f)
            print("\n✅ All Students:")
            print(json.dumps(data, indent=4))
        
  