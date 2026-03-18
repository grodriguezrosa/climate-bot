import  requests
import os
from dotenv import load_dotenv

from models.city import City
from models.weather import Weather

load_dotenv()

url_base = "http://api.openweathermap.org"
owm_key = os.getenv('OWM_KEY')

class OwmService:
    @staticmethod
    def fetch_city(self: str) -> list[City]:
         url = url_base + f"/geo/1.0/direct?q={self}&appid={owm_key}"
         response = requests.get(url)
         return [City.from_dict(item) for item in response.json()]



    @staticmethod
    def obtain_own_data(lat: float, lon: float) -> Weather:
        url = url_base + f"/data/2.5/weather?lat={lat}&lon={lon}&appid={owm_key}"
        respose = requests.get(url)
        return Weather.from_dict(respose.json())
