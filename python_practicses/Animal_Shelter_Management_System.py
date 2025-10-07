# You’ll build a program that simulates how an animal shelter handles different animals using polymorphism.

# Requirements
# 🐾 Base Class: Animal

# Attributes: name, age

# Method:

# make_sound() → should print "Animals make different sounds."

# info() → should print "Name: X, Age: Y"

# 🐶 Child Class: Dog (inherits from Animal)

# Additional attribute: breed

# Override:

# make_sound() → "Woof!"

# info() → include breed in output

# 🐱 Child Class: Cat

# Additional attribute: color

# Override:

# make_sound() → "Meow!"

# info() → include color in output

# 🐦 Child Class: Bird

# Additional attribute: can_fly (True/False)

# Override:

# make_sound() → "Tweet!"

# info() → include flying capability

# 🏢 Class: AnimalShelter

# Attribute: animals → list to store any type of Animal

# Methods:

# add_animal(animal_obj) → adds any animal object

# show_all_animals() → calls info() for each animal

# make_all_sounds() → calls make_sound() for each animal

# find_oldest_animal() → prints the animal with the highest age



class Animal:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def make_sound(self):
        print(f"Animals make different sound")
    def info(self):
        print(f"Name: {self.__name}, Age{self.__age}")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.__breed = breed
    def make_sound(self):
        print("A dog woofs")
    def info(self):
        super().info()
        print(f"{self.__breed}")
class Cat(Animal):
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.__color =color
    def make_sound(self):
         print("A cat meows")
    def info(self):
        super().info()
        print(f"{self.__color}")
class Bird(Animal):
    def __init__(self, name, age,can_fly=False):
        super().__init__(name, age)
        self.__can_fly = can_fly
    def make_sound(self):
       print("A bird Tweet!")
    def info(self):
        super().info()
        if self.__can_fly:
            print(f"{self.__can_fly}")
        else:
            print("Can't Fly")




    

    


        










