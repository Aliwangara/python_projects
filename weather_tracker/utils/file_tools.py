import json
import os

weather_json = 'weather_data.json'

def save_to_json(data, file=weather_json):
    with open(file,'a',newline="") as f:
        json.dump(data,f,indent=4)

def load_from_json(data,file=weather_json):
    if not os.path.exists(file):
        with open(file,'r') as f:
            return json.load(f)
    else:
        []

