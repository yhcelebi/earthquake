# models.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Earthquake(BaseModel):
    id: Optional[str]  # Assuming this is optional because it's generated when inserting into the database
    date: datetime = datetime(1999, 9, 10)
    time: str = "03:01"
    depth: float = 15.0  # unit in kilometers
    latitude: float = 41.015137
    longitude: float = 28.979530
    magnitude: float = 7.6


class EarthquakeCreate(Earthquake):
    pass

