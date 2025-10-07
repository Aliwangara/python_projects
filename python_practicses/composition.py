class Engine:
    def __init__(self, horsepower):
        self.__horsepower = horsepower  # encapsulated

    def get_horsepower(self):
        return self.__horsepower

    def start(self):
        print(f"Engine with {self.__horsepower} HP started!")

class Car:
    def __init__(self, model, engine):
        self.__model = model
        self.__engine = engine  # Composition

    def start_car(self):
        print(f"{self.__model} starting...")
        self.__engine.start()

    def car_info(self):
        print(f"Model: {self.__model}, Engine Power: {self.__engine.get_horsepower()} HP")