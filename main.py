import os
from datetime import datetime
from weather import WeatherFetcher
from logger_config import setup_logging

# Create or get the logger
logger = setup_logging()

def main():
    config_file = 'config.json'
    weather_fetcher = WeatherFetcher(config_file)
    
    city = input("Enter a city name: ")
    success, weather_or_message = weather_fetcher.get_weather(city)
    
    if success:
        print(f"Weather data for {city}:\nTemperature: {weather_or_message['temperature']}°C\n"
              f"Weather Condition: {weather_or_message['condition']}\n"
              f"Humidity: {weather_or_message['humidity']}%")
        logger.info('Successfully retrieved current weather data.')

        see_forecast = input("Would you like to see the 5-day forecast? (yes/no): ").lower()
        if see_forecast == 'yes':
            success, forecast_or_message = weather_fetcher.get_five_day_forecast(city)
            if success:
                print("5-day forecast:")
                for item in forecast_or_message['list']:
                    date = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d %H:%M:%S')
                    temp = item['main']['temp']
                    description = item['weather'][0]['description']
                    print(f"{date}: Temp: {temp}°C, Description: {description}")
                logger.info('Successfully retrieved 5-day forecast.')
            else:
                print(f"Error retrieving forecast: {forecast_or_message['error']}")
                logger.error('Failed to retrieve 5-day forecast.')
    else:
        print(f"Error retrieving weather: {weather_or_message['error']}")
        logger.error('Failed to retrieve current weather.')
        
if __name__ == "__main__":
    main()
