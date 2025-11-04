import datetime
from StudentInfomanager.students import Student
from StudentInfomanager.utils.file_tools import save_to_json,load_from_json
from StudentInfomanager.utils.github_tools import github_data


def student_data():
    students_list = []
    number_of_students = int(input("Enter number of students you want to add:  "))

    for s in range(number_of_students):
        name = input("Enter student's fullname:  ").strip().lower()
        age = int(input("Enter Student's Age:   "))
        email = input("Enter student's Email:  ")
        github_username = input(f"Enter {name}'s github username:   ")
        skills = input("Enter skills separate with comma:  ").strip().split(',')

        student = Student(name,age,email,skills,github_username)

        github_info = github_data(github_username)

        if github_info:
            student_data = student.to_dict()
            student_data.update(github_info)
        else:
            print(f"⚠️ Could not fetch GitHub info for {github_username}")
            student_data = student.to_dict()

        student_data["date_added"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        students_list.append(student_data)
    save_to_json(students_list)

student_data()
        
       


    

