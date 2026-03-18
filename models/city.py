from dataclasses import dataclass

@dataclass
class City:
    name: str
    lat: float
    lon: float
    country: str

    @staticmethod
    def from_dict(obj: dict) -> 'City':
        return City(
            name=obj.get("name"),
            lat=obj.get("lat"),
            lon=obj.get("lon"),
            country=obj.get("country")
        )