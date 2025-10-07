# Requirements
# Class: Engine

# Private Attribute:

# __horsepower (int)

# Methods:

# __init__(self, horsepower) — sets horsepower

# engine_info(self) — prints: "Engine horsepower: XXXX HP"

# Class: Car

# Private Attributes:

# __brand

# __engine → (an Engine object)

# Methods:

# __init__(self, brand, engine) — stores brand and engine

# car_info(self) — prints brand and calls engine.engine_info()

# upgrade_engine(self, new_engine) — replaces the current engine with a new one

# 🚘 Program Flow

# Create an Engine object with 150 horsepower.

# Create a Car object (e.g., "Toyota") and attach that engine.

# Display car info.

# Create a new Engine object with 250 horsepower.

# Upgrade the car’s engine.

# Display car info again to show the new horsepower.

class Engine:
    def __init__(self,horse_power):
        self.__horse_power = int(horse_power)

    def engine_info(self):
        print(f"Engine horsepower: {self.__horse_power}HP")

class Car:
    def __init__(self,brand,engine):
        self.__brand = brand
        self.__engine = engine
    def car_info(self):
        print(f"Brand: {self.__brand}")
        self.__engine.engine_info()
    def upgrade_engine(self, new_engine):
        self.__engine = new_engine

engine1 = Engine(150)
car1 = Car("Toyota", engine1)

car1.car_info()

engine_upgrade =Engine(2000)

car1.upgrade_engine(engine_upgrade)
car1.car_info()

        