import requests
import csv
from datetime import datetime

# Configuration
API_KEY = '0eb7f67cbffc11971bf57f4ca5bdd712'  # Replace with your actual API key
CITY = 'London'  # Replace with your city name
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}"

try:
    # API Call
    response = requests.get(URL)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    data = response.json()

    # File to Save Data
    with open('raw_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Time", "Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)", "Weather Condition"])

        # Process Each Entry
        for entry in data['list']:
            dt = datetime.utcfromtimestamp(entry['dt'])
            date, time = dt.strftime('%Y-%m-%d'), dt.strftime('%H:%M:%S')
            temp = entry['main']['temp'] - 273.15  # Convert Kelvin to Celsius
            humidity = entry['main']['humidity']
            wind_speed = entry['wind']['speed']
            weather = entry['weather'][0]['description']
            writer.writerow([date, time, round(temp, 2), humidity, wind_speed, weather])

    print("Weather data successfully saved to 'raw_data.csv'.")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
except KeyError as key_err:
    print(f"Missing key in response data: {key_err}")
except Exception as e:
    print(f"An error occurred: {e}")
