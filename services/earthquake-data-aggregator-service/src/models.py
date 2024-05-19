from pydantic import BaseModel, UUID4, field_validator
from datetime import datetime
from typing import Optional, List


class EarthquakeGeometry(BaseModel):
    type: str = "Point"
    coordinates: List[float]


class EarthquakeProperties(BaseModel):
    source_id: str
    source_catalog: str
    lastupdate: Optional[datetime] = None  # Optional datetime for last update
    time: datetime
    flynn_region: str
    lat: Optional[float] = None  # Allow lat coming from properties or geometry
    lon: Optional[float] = None  # Allow lon coming from properties or geometry
    depth: float
    evtype: str
    auth: str
    mag: float
    magtype: str
    unid: str


class EarthquakeBase(BaseModel):
    id: Optional[UUID4] = None  # Optional UUID for database insertion
    type: str = "Feature"
    geometry: EarthquakeGeometry
    properties: EarthquakeProperties


class Earthquake(EarthquakeBase):
    @field_validator('geometry', mode='before')
    def set_lat_lon_from_geometry(cls, v, values):
        properties = values.get('properties')
        if properties:
            if properties.lat is None and len(v.coordinates) > 1:
                properties.lat = v.coordinates[1]
            if properties.lon is None and len(v.coordinates) > 0:
                properties.lon = v.coordinates[0]
        return v


class EarthquakeUpdate(Earthquake):
    pass
