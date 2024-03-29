import unittest
import sys
sys.path.append('C:/Users/Desktop/Desktop/Estudo/Weather-API')
from weather import WeatherFetcher
from unittest.mock import patch
import requests


class TestWeatherFetcher(unittest.TestCase):

    def setUp(self):
        # Setup code runs before each test method
        self.fetcher = WeatherFetcher('config.json')

    def test_get_weather_valid_city(self):
        # Test get_weather with a valid city
        result, message = self.fetcher.get_weather('London')
        self.assertTrue(result)

    def test_get_weather_invalid_city(self):
        # Test get_weather with an invalid city
        result, message = self.fetcher.get_weather('InvalidCityName123')
        self.assertFalse(result)
    
    def test_get_weather_empty_city(self):
        # Test get_weather with an invalid city when is empty
        result, message = self.fetcher.get_weather('')
        self.assertFalse(result)
        self.assertIn("City name cannot be empty", message)

    def test_get_weather_none_city(self):
        # Test get_weather with an invalid city when is none
        result, message = self.fetcher.get_weather(None)
        self.assertFalse(result)
        self.assertIn("City name must be a string", message)

    @patch('weather.requests.get')
    def test_get_weather_api_key_error(self, mock_get):
        # Set up the mock to raise an HTTPError when `raise_for_status` is called
        mock_response = mock_get.return_value
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("401 Client Error: Unauthorized for url")

        # Make the .json() method of the mock return a specific message
        mock_response.json.return_value = {"cod": 401, "message": "Invalid API key"}

        result, message = self.fetcher.get_weather('London')
        self.assertFalse(result)
        self.assertIn("Invalid API key", message)


    # ... Additional test cases ...

if __name__ == '__main__':
    unittest.main()
