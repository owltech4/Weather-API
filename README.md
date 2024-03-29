Weather-API Documentation
=========================

Overview
--------

Weather-API is a Python project that allows users to fetch the current weather information for any city using the OpenWeatherMap API.

Features
--------

*   Fetch current weather by city name.
*   Return temperature, weather conditions, and humidity.
*   Error handling for invalid city names and API keys.

Prerequisites
-------------

*   Python 3.8 or above.
*   `requests` library (Install using `pip install requests`).
*   OpenWeatherMap API key.

Installation
------------

Clone the repository to your local machine:

shCopy code

`git clone https://github.com/yourusername/Weather-API.git cd Weather-API`

Install the required packages:

shCopy code

`pip install -r requirements.txt`

Configuration
-------------

1.  Rename `config.json.example` to `config.json`.
2.  Replace the placeholder in `config.json` with your OpenWeatherMap API key.

jsonCopy code

`{     "api_key": "YOUR_API_KEY",     "base_url": "http://api.openweathermap.org/data/2.5/weather",     "units": "metric" }`

Alternatively, you can set the API key as an environment variable `WEATHER_API_KEY`.

Usage
-----

To use the Weather-API, run the `main.py` script and enter the city name when prompted:

shCopy code

`python main.py`

Testing
-------

To run tests, execute:

shCopy code

`python -m unittest discover -s test`

Modules Description
-------------------

### main.py

This is the entry point of the application. It interacts with the user and uses the `WeatherFetcher` class to fetch and display weather data.

### weather.py

Contains the `WeatherFetcher` class which handles the communication with the OpenWeatherMap API.

### logger\_config.py

Configures the logging system for the application, saving logs to `app.log`.

### config.json

Stores configuration settings such as the API key, base URL, and measurement units.

### test/

Contains the `test_weather.py` script which holds unit tests for the `WeatherFetcher` class.

Contributing
------------

To contribute to Weather-API, please ensure you follow the guidelines in CONTRIBUTING.md.
