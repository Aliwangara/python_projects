# Add student

# Ask for student’s name.

# Ask for age.

# Ask for scores in 3 subjects (store as a list).

# Save all in a dictionary inside a list.

# Example:

# {"name": "Ali", "age": 20, "scores": [85, 90, 78]}


# View all students
# Print each student’s details like:

# 1. Ali → Age: 20 → Scores: [85, 90, 78]


# Search student by name
# If found, show details.
# If not, print "Student not found".

# Update student

# Choose student by number.

# Options:

# Update age

# Add new score (+)

# Remove last score (-)

# Find top student
# Use max(..., key=lambda ...) to find the student with the highest average score.

# Sort students

# Sort by name (A–Z)

# Sort by average score (highest → lowest)

# Exit the program

student_result_list = []
def add_Student():
    name = input("Enter name of the student:   ").lower()
    age =  int(input("Enter students age:   "))
    score = input("Enter students 3 scores eg(70 80 90):    ")
    student_info = {
        "name":name,
        "age": age,
        "score": list(map(int, score.split()))
    }
    student_result_list.append(student_info)
    print(student_result_list)


def view_students():
    if student_result_list:
     for student in student_result_list:
        print(f"Name: {student['name']} -> Age: {student['age']} -> Scores: {student['score']}")
    else:
       print("No students added in the list")


def update_student():
   for i, student in enumerate(student_result_list,1):
      print(f"{i}. {student}")
    
   student_selection = int(input("Select students by number above:  "))-1
   
   if 0<= student_selection < len(student_result_list):
      print("1.Update age")
      print("2.Update Score")

      option = int(input("Enter number of option you want to choose from the ones above:  "))

      if option == 1:
         operation = input("Enter operation you want to use(+ or -): ")
         update_age = int(input("Update students age:  "))
         if operation == "+":
            student_result_list[student_selection]['age'] += update_age
         elif operation == "-":
            student_result_list[student_selection]['age'] -= update_age
         else:
            print("Please select the correct operation")
         print(f"Updated {student_result_list[student_selection]['name']} age to {student_result_list[student_selection]['age']}")
      elif option ==2:
         operation = input("Enter operation you want to use(+ or -): ")
         score_index = int(input("Enter the index of the number you want to change(1,2 or 3 ):   "))
         remove_las_score = input("Type (y)to remove the last score /(n) to continue: ").lower()
         update_score = int(input("Update students Score:  "))
         if score_index == 1 and operation == "+":
            student_result_list[student_selection]['score'][0] += update_score
         elif score_index == 2 and operation == "+":
            student_result_list[student_selection]['score'][1] += update_score
         elif score_index == 3 and operation == "+":
            student_result_list[student_selection]['score'][2] += update_score

            # Score reduction operations
         elif score_index == 1 and operation == "-":
            student_result_list[student_selection]['score'][0] -= update_score
         elif score_index == 2 and operation == "-":
            student_result_list[student_selection]['score'][1] -= update_score
         elif score_index == 3 and operation == "-":
            student_result_list[student_selection]['score'][2] -= update_score
         elif remove_las_score == "y":
             student_result_list.remove(student_result_list[student_selection]['score'][2])
         elif remove_las_score =='n':
            print("You aren't removing the last score")
         else:
            print("please the correct operation")  
         print(f"Updated: {student_result_list[student_selection]['name']} Score: {student_result_list[student_selection]['score']}")
      else:
         print("please choose from the options provided above")
   else:
      print("Choose number input please from the list")
      


def top_student():
   
   first_student = max(student_result_list, key=lambda s: sum(s['score']))
   print(f"Top Score: {first_student}")
   
   


def sort_students():
   
   sort_by_name = sorted(student_result_list, key=lambda s: (s['name'], sum(s['score'])/len(student_result_list)))
   print(f'Sorted: {sort_by_name}')


while True:
   print("1. add Student")
   print("2. view students")
   print("3. update student")
   print("4. top student")
   print("5. sort students")
   print("6. Exit")

   student_input = int(input("Choose a number from the option above:  "))

   if student_input == 1:
       add_Student()
   elif student_input ==2:
      view_students()
   elif student_input == 3:
      update_student()
   elif student_input == 4:
      top_student()
   elif student_input ==5:
      sort_students()
   elif student_input == 6:
      print(f"------ Thank You -------")
      break
   else:
      print("please Select the available Inputs")
    
    