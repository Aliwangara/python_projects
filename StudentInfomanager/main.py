


students_list = []

def student_data():
    number_of_students = int(input("Enter number of students you want to add:  "))

    for s in range(number_of_students):
        name = input("Enter student's fullname:  ").strip().lower()
        age = int(input("Enter Student's Age:   "))
        email = input("Enter student's Email:  ")
        github_username = input(f"Enter {name}'s github username:   ")
        skills = input("Enter skills separate with comma:  ").strip().split(',')

        students_dict = {
            "name":name,
            "age":age,
            "email":email,
            "github_username":github_username,
            "skills":skills
        }
        students_list.append(students_dict)
    print(students_list)
# if __name__ == "main.py":
student_data()
