import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  # Added &units=metric for Celsius
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        
        weather_data = response.json()
        
        # Extracting specific data points
        temp = weather_data['main']['temp']
        weather_condition = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        
        return (True, f"Temperature: {temp}°C\nWeather Condition: {weather_condition}\nHumidity: {humidity}%")
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            return (False, "City not found. Please check the city name and try again.")
        else:
            return (False, "An error occurred while retrieving the weather data.")
    except Exception as e:
        return (False, "An error occurred: " + str(e))

def main():
    api_key = 'YOUR_API_KEY_HERE'
    city = input("Enter a city name: ")
    success, message = get_weather(api_key, city)
    if success:
        print("Weather data for", city + ":\n" + message)
    else:
        print(message)

if __name__ == "__main__":
    main()
