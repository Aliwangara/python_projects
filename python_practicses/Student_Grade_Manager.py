# Add a student → ask for name and score.

# View all students → show names + scores.

# Search a student by name.

# Find top scorer → show the student with the highest score.

# Exit






students_list = []

def add_student():
    name  = input("Enter student name:   ").lower()
    score = int(input("Enter student Score:  ")) 

    student_info = {
    "name": name,
    "score": score
    }

    students_list.append(student_info)
    
add_student()

def view_students():
    for student in students_list:
        print(f"Students are: {student}")
view_students()

def search_student():
    search_name = input("Enter name of the student you want to search:  ").lower()

    for search in students_list:
        if search_name in search["name"]:
            print(f"{search_name} Scored: {search['score']}")
            
search_student()

def top_scorer():
    if students_list:
         top = max(students_list, key = lambda s:s["score"])
         print(f"The top student is {top['name']} with score {top['score']}")
    else:
        print("There is nothing in the list")
top_scorer()

while True:
    print("1. Add Student")
    print("2. view Student")
    print("3. Search Student")
    print("4. View Top Student")
    print("5. Exit")

    enter_option = input("Choose an option(1-5):    ")

    if enter_option == "1":
        add_student()
    elif enter_option == "2":
        view_students()
    elif enter_option == "3":
        search_student()
    elif enter_option == "4":
        top_scorer()
    elif enter_option == "5":
        print("---- Thank You -----")
        break
    else:
        print("====== Please select on option from the ones Above =====")
        
    






