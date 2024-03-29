import os
from weather import WeatherFetcher
from logger_config import setup_logging

# Create or get the logger
logger = setup_logging()

# Use the logger
logger.info('Starting the code...')

def main():
    config_file = 'config.json'
    weather_fetcher = WeatherFetcher(config_file)
    #api_key = os.getenv('teste-api', 'c3fb11839567417b1091f3c0f978bdd1')
    #weather_fetcher = WeatherFetcher(api_key)
    
    city = input("Enter a city name: ")
    success, message = weather_fetcher.get_weather(city)
    
    if success:
        print("Weather data for", city + ":\n" + message)
        # Use the logger
        logger.info('This run was a success!')
    else:
        print(message)
        logger.info('Sorry, but does not work right!')

if __name__ == "__main__":
    main()
