

class Student:
    def __init__(self,name,age,email,github_username):
        self.__name = name
        self.__age = age
        self.__email = email
        self.__github_username = github_username

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_email(self):
        return self.__email
    def get_github_username(self):
        return self.__github_username