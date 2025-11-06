from weather_tracker.weather import Weather
from weather_tracker.utils import api_tools
from weather_tracker.utils.file_tools import save_to_json,load_from_json

class CityNameError(Exception):
      pass


city_name = input("Enter name of the city: ")
    
          

weather_info = api_tools.weather_api(city_name)


if weather_info:
    weather = Weather(
        city = weather_info['city'],
        temperature=weather_info['Temp'],
        humidity=weather_info['Humidity'],
        description=weather_info['Description'],
        timestamp= weather_info['date']


    )


    weather_data = weather.to_dict()
    save_to_json(weather_data)
else:
        print(f"⚠️ Could not fetch Weather info for {city_name}")

    


