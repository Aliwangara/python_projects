

def student_data():
    students_list = []
    number_of_students = int(input("Enter number of students you want to add:  "))

    for s in range(number_of_students):
        name = input("Enter student's fullname:  ").strip().lower()
        age = int(input("Enter Student's Age:   "))
        email = input("Enter student's Email:  ")
        github_username = input(f"Enter {name}'s github username:   ")
        skills = input("Enter skills separate with comma:  ").strip().split(',')

        students_dict = {
            "name":name.title(), 
            "age":age,
            "email":email,
            "github_username":github_username,
            "skills":skills
        }
        students_list.append(students_dict)
    return students_list


    

