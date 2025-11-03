
students_file = "students.txt"
class Student:
    def __init__(self, student_id, name,score):
        self.__id = student_id
        self.__name = name
        self.__score = list(map(int,score))
    
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score 
    
    def calculate_average(self):
        return sum(self.__score) / len(self.__score)
    
    def get_grade(self):
        avg = self.calculate_average()
        if   80 >= avg <= 100:
            grade = "A"
        elif 70>=  avg <= 79:
            grade = "B"   
        elif  60 >=  avg <= 69:
            grade = "C"
        elif  50 >= avg <= 59:
            grade = "D"
        else:
            grade = "F"
        return grade



# student_id = input("Enter student Id: ")
# name = input("Enter Students name: ")
# score = input("Enter 3 separate marks using a space: ").split()

# student = Student(student_id,name,score)

# with open(students_file,'w') as f:
#     f.write("Id Name  Average Grade\n")

# with open(students_file,'a',newline="") as f:
#     f.write(f"{student.get_id()} {student.get_name()}, {student.calculate_average():.2f}, {student.get_grade()}\n")

with open(students_file, 'r') as f:
    print("ID       Name          Average   Grade")
    print('-'*40)

    for line in f:
      print(line.strip())



    

        
       


        
    

         