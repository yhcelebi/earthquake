# models.py

import datetime
import uuid

from uuid import UUID
from pydantic import BaseModel


class EarthquakeBase(BaseModel):
    id: UUID = uuid.uuid4()
    date: str = f"{datetime.datetime(1999, 9, 10)}"
    time: str = f"{datetime.time(3, 1)}"
    depth: float = 15.0  # unit in kilometers
    latitude: float = 41.015137
    longitude: float = 28.979530
    magnitude: float = 7.6
