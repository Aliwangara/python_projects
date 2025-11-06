
class Weather:
    def __init__(self,city,temperature,humidity,description,timestamp):
        self.__city = city
        self.__temperature = temperature
        self.__humidity = humidity
        self.__description = description
        self.__timestamp = timestamp
    def get_city(self):
        return self.__city
    def get_temperature(self):
        return self.__temperature
    def get_humidity(self):
        return self.__humidity
    def get_description(self):
        return self.__description
    def get_timestamp(self):
        return self.__timestamp
    
    def display_info(self):
        print(f"City: {self.__city},\nTemperature: {self.__temperature},\nHumidity: {self.__humidity},\ndescription: {self.__description}\nDate: {self.__timestamp}")
    
    def to_dict(self):
        return {
            "city": self.__city,
            "temperature": self.__temperature,
            "humidity": self.__humidity,
            "description": self.__description,
            "date": self.__timestamp
        }
    