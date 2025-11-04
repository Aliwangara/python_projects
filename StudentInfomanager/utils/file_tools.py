import os
import json




students_file = "students.json"

def save_to_json(data,file=students_file):
    with open(file,'a') as f:
        json.dump(data,f,indent=4)

def load_from_json(file=students_file):    
    if not os.path.exists(students_file):
        with open(file,'r') as f:
            return json.load(f)
    return []


