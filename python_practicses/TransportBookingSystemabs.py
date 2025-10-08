# Abstract Base Class: Vehicle

# Private Attributes:

# __brand

# __max_speed

# Methods:

# __init__(self, brand, max_speed)

# get_brand() → returns the brand

# get_max_speed() → returns max speed

# vehicle_info() → prints “Brand: X, Max Speed: Y km/h”

# @abstractmethod → calculate_fare(distance) → must be implemented by all subclasses

# Subclass: Car

# Additional private attribute: __rate_per_km

# Methods:

# __init__(self, brand, max_speed, rate_per_km)

# Override calculate_fare(distance) → fare = distance * rate_per_km

# Override vehicle_info() to include rate per km

# Subclass: Bike

# Additional private attribute: __rate_per_km

# Methods:

# __init__(self, brand, max_speed, rate_per_km)

# Override calculate_fare(distance) → fare = distance * rate_per_km

# Override vehicle_info() to include rate per km

# Subclass: Bus

# Additional private attribute: __rate_per_km

# Methods:

# __init__(self, brand, max_speed, rate_per_km)

# Override calculate_fare(distance) → fare = distance * rate_per_km

# Override vehicle_info() to include rate per km

# 🧩 Program Flow

# Create three objects:

# Car("Toyota", 180, 20)

# Bike("Yamaha", 120, 10)

# Bus("Volvo", 100, 50)

# Store them in a list.

# Loop through each vehicle and:

# Display vehicle info.

# Calculate and print fare for a 50 km trip.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self,brand,max_speed):
        self.__brand = brand
        self.__max_speed = max_speed
    def get_brand(self):
        return self.__brand
    def get_max_speed(self):
        return self.__max_speed
    def vehicle_info(self):
        print(f"Brand: {self.get_brand()}, Max Speed: {self.get_max_speed()}KM/H")
    
    @abstractmethod
    def calculate_fare(self,distance):
        pass


class Car(Vehicle):
    def __init__(self, brand, max_speed,rate_per_km):
        super().__init__(brand, max_speed)
        self.__rate_per_km = rate_per_km
    def calculate_fare(self, distance):
         super().calculate_fare(distance)
         fare = distance * self.__rate_per_km
         return fare
    def vehicle_info(self):
        super().vehicle_info()
        print(f"Rate Per Km: {self.__rate_per_km}")

class Bike(Vehicle):
    def __init__(self, brand, max_speed,rate_per_km):
        super().__init__(brand, max_speed)
        self.__rate_per_km = rate_per_km
    def calculate_fare(self, distance):
        super().calculate_fare(distance)
        fare = distance * self.__rate_per_km
        return fare
    def vehicle_info(self):
        super().vehicle_info()
        print(f"Rate_per_km: {self.__rate_per_km}")
class Bus(Vehicle):
    def __init__(self, brand, max_speed,rate_per_km):
        super().__init__(brand, max_speed)
        self.__rate_per_km = rate_per_km
    def calculate_fare(self, distance):
        super().calculate_fare(distance)
        fare  = distance * self.__rate_per_km
        return fare
    def vehicle_info(self):
        super().vehicle_info()
        print(f"Rate_per_km: {self.__rate_per_km}")

car = Car("Toyota", 180, 20)
bike = Bike("Yamaha", 120, 10)
bus = Bus("Volvo", 100, 50)

v_info = [car,bike,bus]

for v in v_info:
    v.vehicle_info()
    fare = v.calculate_fare(50)
    print(f"Fare for 50 km: ${fare}")
    print("-" * 40)
    
    
    
    



