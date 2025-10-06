# Create a Car class with:

# attributes: name, make, yom

# method: car_info()

# Create a child class SportsCar(Car) that adds:

# attribute: top_speed

# method: show_speed() that prints "Top speed is XXX km/h"

# Create an object of SportsCar and call both methods:

# car_info()

# show_speed()




class Car:
    def __init__(self,name,make,yom):
        self.__name = name
        self.__make = make
        self.__yom = yom
    def car_info(self):
        print(f"Name: {self.__name}\nMake: {self.__make}\nYOM: {self.__yom}")
class SportsCar(Car):
    def __init__(self, name,make,yom,top_speed):
        super().__init__(name,make,yom)
        self.__name = name
        self.__make = make
        self.__yom = yom
        self.__topspeed = top_speed
    def show_speed(self):
        print(f"{self.__name} {self.__make} is moving at {self.__topspeed}KPH")

car1 = SportsCar("Mazda", "Axela", "2021", 200)

car1.show_speed()
        