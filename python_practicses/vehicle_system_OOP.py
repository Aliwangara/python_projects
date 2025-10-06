# Task

# You are to design a small OOP program to manage vehicles in a transport company.
# Follow these instructions carefully 👇

# 🚗 1. Base Class: Vehicle

# Attributes (make them private):

# __name

# __brand

# __year

# Methods:

# vehicle_info() → prints name, brand, and year

# set_year(new_year) → only accepts years greater than 2000, otherwise print "Invalid year!"

# update_name(new_name) → changes vehicle name

# 🚙 2. Child Class: Car (inherits from Vehicle)

# Additional Attribute:

# __num_doors

# Additional Methods:

# show_doors() → prints how many doors the car has

# Override the vehicle_info() method:

# Include number of doors in the info.

# 🏎️ 3. Child Class: SportsCar (inherits from Car)

# Additional Attribute:

# __top_speed

# Additional Methods:

# show_speed() → prints top speed in km/h

# Override vehicle_info() again:

# Include top speed in the output along with other details.

# 🚧 4. Usage Example

# Create objects:

# A Vehicle named “Lorry”, brand “Mercedes”, year 2019

# A Car named “Sedan”, brand “Toyota”, year 2021, with 4 doors

# A SportsCar named “Supra”, brand “Toyota”, year 2022, with 2 doors and top speed 320 km/h

# Then:

# Call vehicle_info() on each object

# Try to set an invalid year for one of them

# Show the specific methods (show_doors(), show_speed())

class Vehicle:
    def __init__(self,name,brand,year):
        self.update_name(name)
        self.__brand = brand
        self.set_year(year)
        
    def vehicle_info(self):
        print(f"Name: {self.__name}\nBrand: {self.__brand}\nYOM: {self.__year}")
    def set_year(self,new_year):
        if new_year > 2000:
         self.__year = new_year
        else:
           print("Invalid year")
    def get_year(self):
       return f"{self.__year}"
    def update_name(self, updated_name):
       self.__name = updated_name

vehicle1 = Vehicle("Mercedes", "A180",2001)
vehicle1.vehicle_info()