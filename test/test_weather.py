import unittest
import sys
sys.path.append('C:/Users/Desktop/Desktop/Estudo/Weather-API')
from weather import WeatherFetcher


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
    
    # ... Additional test cases ...

if __name__ == '__main__':
    unittest.main()
