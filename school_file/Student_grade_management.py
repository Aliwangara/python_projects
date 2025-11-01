

class Student:
    def __init__(self, student_id, name,score):
        self.__id = student_id
        self.__name = name
        self.__score = map(int,list(score))
    
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    
    def calculate_average(self):
       return sum(self.get_score())/ len(self.get_score())
    
    

         