from dataclasses import dataclass


@dataclass
class City:
    """Stores the information for one city."""

    city_id: int
    name: str
    latitude: float
    longitude: float
    population: int
    distance: float