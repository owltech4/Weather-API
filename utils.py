# utils.py
import csv
from datetime import datetime

class WeatherDataRecorder:
    def __init__(self, filename="weather_data.csv"):
        self.filename = filename
        self.headers = ['date', 'city', 'temperature (°C)', 'condition', 'humidity (%)']

    def append_weather_to_csv(self, city,weather_data):
        with open(self.filename, 'a+', newline='') as csvfile:
            csvfile.seek(0)
            file_is_empty = (csvfile.read(1) == '')
            csvfile.seek(0)
            writer = csv.writer(csvfile)
            if file_is_empty:
                writer.writerow(self.headers)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                city,
                weather_data['temperature'],
                weather_data['condition'],
                weather_data['humidity']
            ])
