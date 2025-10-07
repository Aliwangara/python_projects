# Requirements

# Class: Battery

# Private attribute: __capacity (in mAh)

# Method:

# battery_info() → prints "Battery capacity: XXXX mAh"

# Class: Laptop

# Private attributes:

# __brand

# __battery → will hold a Battery object

# Methods:

# laptop_info() → prints "Laptop brand: X" and calls the battery’s battery_info()

# replace_battery(new_battery) → replaces the existing battery with a new one

# Program Flow:

# Create a Battery object (e.g., 5000 mAh)

# Create a Laptop object (e.g., Dell) and pass in the battery

# Display laptop info

# Replace the battery with a new one (e.g., 7000 mAh)

# Display laptop info again


class Battery:
    def __init__(self,capacity):
        self.__capacity = capacity

    def get_capacity(self):
        return self.__capacity

    def battery_info(self):
        print(f"Battery Capacity: {self.__capacity} mAH")


class Laptop:
    def __init__(self, brand, battery):
        self.__brand = brand
        self.__battery = battery

    def get_brand(self):
        return self.__brand

    def get_battery(self):
        return self.__battery

    def laptop_info(self):
        print(f"Laptop Brand: {self.__brand}")
        self.__battery.battery_info()

    def replace_battery(self, new_battery):
        self.__battery = new_battery


battery1 = Battery(5000)
laptop1 = Laptop("dell", battery1)

laptop1.laptop_info()

battery2 = Battery(7000)
laptop1.replace_battery(battery2)

laptop1.laptop_info()