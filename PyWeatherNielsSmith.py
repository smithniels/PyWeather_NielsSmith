'''this file retrieves weather data for the selected city'''

import requests

CITY_NAME = "Copenhagen"
API_KEY = "290a1bec5e623e9a6791b687e8f47bd3"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    temperature_kelvin = weather_data["main"]["temp"]
    weather_description = weather_data["weather"][0]["description"]
    temperature_celsius = temperature_kelvin - 273.15
    temperature_celsius = round(temperature_celsius, 2)
    temperature_fahrenheit = round((temperature_celsius*9/5)+32, 2)
    # humidity = weather_data["main"]["humidity"]
    print(f"Temperature: {temperature_celsius} Celsius")
    print(f"Temperature: {temperature_fahrenheit} Farhrenheit")
    print(f"Weather: {weather_description}")
    # print(f"Humidity: {humidity}")
else:
    print("Failed to fetch weather data.")
