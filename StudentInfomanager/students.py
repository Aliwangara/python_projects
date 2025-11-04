import json

class Student:
    def __init__(self,name,age,email,skills,github_username):
        self.__name = name
        self.__age = age
        self.__email = email
        self.__skills = skills
        self.__github_username = github_username

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_email(self):
        return self.__email
    def get_skills(self):
        return self.__skills
    def get_github_username(self):
        return self.__github_username
    
    def display_info(self):
        print(f"Name: {self.__name}\nAge: {self.__age}\nEmail: {self.__email}\nGithub Username: {self.__github_username}")

    def to_dict(self):
        student_dict = {
            "name": self.__name,
            "age": self.__age,
            "email": self.__email,
            "github_username": self.__github_username

        }
        return student_dict
