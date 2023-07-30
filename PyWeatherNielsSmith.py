import requests

API_Key = "290a1bec5e623e9a6791b687e8f47bd3"
city_name = "Copenhagen"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}"
response = requests.get(url)


if response.status_code == 200:
    weather_data = response.json()
    # Now you have the weather data in the 'weather_data' variable
    print(weather_data)
else:
    print("Failed to fetch weather data.")
