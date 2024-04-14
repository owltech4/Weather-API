import requests
from typing import Tuple, Dict
import json
import os

class WeatherFetcher:
    def __init__(self, config_file):
        with open(config_file, 'r') as config:
            config_data = json.load(config)
        self.api_key = os.getenv('WEATHER_API_KEY', config_data['api_key'])
        self.base_url = "http://api.openweathermap.org/data/2.5"
        self.units = config_data['units']
    
    def get_weather(self, city: str) -> Tuple[bool, Dict]:
        url = f"{self.base_url}/weather?q={city}&appid={self.api_key}&units={self.units}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            weather = {
                'temperature': data['main']['temp'],
                'condition': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'coord': data['coord']
            }
            return True, weather
        except requests.exceptions.RequestException as e:
            return False, {'error': str(e)}

    def get_five_day_forecast(self, city: str) -> Tuple[bool, Dict]:
        url = f"{self.base_url}/forecast?q={city}&appid={self.api_key}&units={self.units}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            forecast_data = response.json()
            # Process the data to extract or summarize daily forecasts
            return True, forecast_data
        except requests.exceptions.RequestException as e:
            return False, {'error': str(e)}
