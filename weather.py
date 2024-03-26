import requests
from typing import Tuple  # Import Tuple from typing

class WeatherFetcher:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.units = "metric"
    
    # Change the return type annotation here
    def get_weather(self, city: str) -> Tuple[bool, str]:
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
