import requests
import datetime


def weather_api(city,api_key=''):
    weather_info = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
    data = weather_info.json()
    print()
    print()
    now = datetime.datetime.now()
    data_json = {
        "city":data.get("name"),
        "Temp":data.get('main')['temp'],
        "Humidity":data.get('main')['humidity'],
        "Description": data.get("weather")[0]['description'],
        "date": now.strftime("%d-%m-%Y, %H:%M:%S")
    }
    print(data_json)
    return data_json
weather_api(city = input("Enter name of the city you want to check weather:  "))