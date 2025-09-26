# Assignment — Student Report System

# You’ll build a CLI program that manages students and their scores.

# Features to include:

# Add a student

# Ask for student’s name.

# Ask for 3 scores (integers).

# Store them in a dictionary like:

# {"Ali": [85, 90, 78]}


# View all students

# Print each student with their scores and their average.

# Search for a student

# Ask for a name.

# If found, show their scores + average.

# Top student

# Use max(..., key=lambda ...) to find the student with the highest average score.

# Sort students

# Option to sort students by:

# Name (A–Z)

# Average score (highest → lowest)

# Exit

students = []

def add_student():
    name = input("Enter name of the student:    ").lower()
    scores = input("Enter student scores eg:(85 90 78):    ")

    student_info = {
        "name":name,
        "score":list(map(int,scores.split()))
    }
    students.append(student_info)




def view_all_students():
   for student in students:
    print(f"{student["name"]}'s scores are {student["score"]} with an average of {sum(student["score"]) / len(student["score"]):.2f}")


def search_students():
   name_search = input("Enter name of the student:   ").lower()
   for student in students:
      if name_search in student['name']:
         print(f"{name_search}'s score is {student['score']}, with an average of {sum(student["score"]) / len(student["score"])} ")
      else:
         print(f"{name_search} not in list")


def top_student():
   
   highest_score = sorted(students,key=lambda x:sum(x['score'])/len(x['score']))
   print(f" score {highest_score}")
   
   



while True:
   print("1. ADD STUDENT")
   print("2. VIEW ALL STUDENTS")
   print("3. SEARCH STUDENT")
   print("4. TOP STUDENT")
   print("5. Exit")

   user_option = input("Enter an option from the ones above (1-4):   ")

   if user_option == "1":
      add_student()
   elif user_option == "2":
      view_all_students()
   elif user_option == "3":
      search_students()
   elif user_option == "4":
      top_student()
   elif user_option == "5":
      print("Thank you!!")
      break
   else:
      print("Option not available please select options from above")
      