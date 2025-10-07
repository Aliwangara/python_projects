# Base Class: Vehicle

# Attributes (make them private):

# __name

# __brand

# __year

# Methods:

# vehicle_info() → prints name, brand, and year

# set_year(new_year) → only accepts years > 2000

# update_name(new_name) → updates vehicle name

# 🚗 2️⃣ Child Class: Car (inherits from Vehicle)

# Additional attribute:

# __num_doors

# Methods:

# show_doors() → prints how many doors the car has

# Override vehicle_info() → include number of doors

# 🏎️ 3️⃣ Child Class: SportsCar (inherits from Car)

# Additional attribute:

# __top_speed

# Methods:

# show_speed() → prints top speed

# Override vehicle_info() again to include top speed

# 🏢 4️⃣ Class: TransportCompany

# This is a new concept — composition
# (The company has many vehicles, not inherits from them.)

# Attributes:

# __name

# __vehicles (a list that stores Vehicle, Car, or SportsCar objects)

# Methods:

# add_vehicle(vehicle_obj) → adds a vehicle to the company list

# show_all_vehicles() → prints info of all vehicles

# find_fastest_vehicle() → prints the car with the highest top speed (only checks SportsCar objects)

# remove_vehicle(name) → removes a vehicle by its name


class Vehicle:
    def __init__(self,name,brand,year):
        self.update_name(name)
        self.__brand = brand
        self.set_year(year)
    def vehicle_info(self):
        print(f"Name: {self.__name}")
        print(f"Brand: {self.__brand}")
        print(f"Year: {self.__year}")
    def set_year(self,new_year):
        if new_year > 2000:
          self.__year = new_year
        else:
            print("Invalid Year")
    def update_name(self, new_name):
        self.__name = new_name
class Car(Vehicle):
    def __init__(self, name, brand, year,num_dooors):
        super().__init__(name, brand, year)
        self.__num_doors = num_dooors
    def show_doors(self):
        print(f"Top Speed: {self.__num_doors}")
    def vehicle_info(self):
        super().vehicle_info()
        print(f"Top Speed: {self.__num_doors}")

class SportsCar(Car):
    def __init__(self, name, brand, year,num_dooors,top_speed):
        super().__init__(name, brand, year,num_dooors)
        self.__top_speed = top_speed
    def show_speed(self):
        super().vehicle_info()
        print(f"Top speed: {self.__top_speed}")



# Polymorphism
        


        


        




