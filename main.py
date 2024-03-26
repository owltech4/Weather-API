# main.py

import os
from weather import WeatherFetcher

def main():
    api_key = os.getenv('teste-api', 'c3fb11839567417b1091f3c0f978bdd1')
    weather_fetcher = WeatherFetcher(api_key)
    
    city = input("Enter a city name: ")
    success, message = weather_fetcher.get_weather(city)
    
    if success:
        print("Weather data for", city + ":\n" + message)
    else:
        print(message)

if __name__ == "__main__":
    main()
