import os
import requests
from dotenv import load_dotenv

from models.city import City
from models.weather import Weather

load_dotenv()

url_base = "http://api.openweathermap.org"
owm_key = os.getenv('OWM_KEY')

def fetch_cities(city: str) -> list[City]:
    url = f'{url_base}/geo/1.0/direct?q={city}&appid={owm_key}'
    response = requests.get(url)
    return [City.from_dict(item) for item in response.json()]

def fetch_weather_data(lat: float, lon: float) -> Weather:
    url = f'{url_base}/data/2.5/weather?lat={lat}&lon={lon}&appid={owm_key}&units=metric'
    response = requests.get(url)
    return Weather.from_dict(response.json())

def format_response(city: str) -> str:
    cities = fetch_cities(city)
    if not cities: return 'Ciudad no encontrada'
    weather = fetch_weather_data(lat=cities[0].lat, lon=cities[0].lon)

    return f'''El tiempo en {cities[0].name} es de {weather.main.temp}ºC con una maximas de {weather.main.temp_max}ºC y unas minimas de {weather.main.temp_min}ºC'''
