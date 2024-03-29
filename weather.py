import requests
from typing import Tuple  # Import Tuple from typing
import json
import os

class WeatherFetcher:
    def __init__(self, config_file):
        with open(config_file, 'r') as config:
            config_data = json.load(config)
        self.api_key = os.getenv('teste-api', config_data.get('api_key'))
        self.base_url = config_data['base_url']
        self.units = config_data['units']
    
    # Change the return type annotation here
    def get_weather(self, city: str) -> Tuple[bool, str]:
        # Handle empty string or None for the city name
        if not city or city is None:
            return False, "City name cannot be empty" if city == '' else "City name must be a string"
        url = f"{self.base_url}?q={city}&appid={self.api_key}&units={self.units}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            weather_data = response.json()
            
            if all(key in weather_data for key in ['main', 'weather']):
                temp = weather_data['main']['temp']
                weather_condition = weather_data['weather'][0]['description']
                humidity = weather_data['main']['humidity']
                return True, f"Temperature: {temp}°C\nWeather Condition: {weather_condition}\nHumidity: {humidity}%"
            else:
                return False, "Incomplete weather data received."
        except requests.exceptions.HTTPError:
            error_message = response.json().get('message', 'An error occurred while retrieving the weather data.')
            return False, f"HTTP Error: {error_message}"
        except Exception as e:
            return False, f"An error occurred: {str(e)}"
