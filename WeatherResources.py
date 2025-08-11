import requests
from geopy.geocoders import Nominatim

# Replace with your OpenWeatherMap API key
api_key = "be57c8ed3edc07427eb5347109c585f9"

def get_weather_data(latitude, longitude):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": "imperial"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        city = data["name"]
        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        print(f"Weather in {city}: {temperature}°F, {weather_desc}")
    else:
        print("Error fetching weather data")

def get_weather_for_city(city):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)
    if location:
        latitude, longitude = location.latitude, location.longitude
        get_weather_data(latitude, longitude)
    else:
        print("City not found")

# Ask the user for a city
city = input("Enter the city to check the weather for: ")
get_weather_for_city(city)

