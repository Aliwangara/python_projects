import requests
Api_key = ""
city = input("Enter the city:  ").capitalize()
# units = input("Enter Unit (C OR  F)").upper()

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api_key}"
# url = f"http://api.openweathermap.org/data/2.5/weather?&appid={Api_key}"


def get_weather():
    
    info = requests.get(url)
    weather_info = info.json()
    location_info =  weather_info.get("weather")
    print(location_info)
    
get_weather()
