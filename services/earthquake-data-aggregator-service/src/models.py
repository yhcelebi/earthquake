#models.py

from uuid import uuid4
from sqlalchemy import Column, Integer, String, Index
from sqlalchemy.dialects.postgresql import UUID, BYTEA
from database import Base
from sqlalchemy import text
from sqlalchemy.schema import DDL

class Earthquake:
    def __init__(self, id, date, latitude, longitude, depth, type, magnitude):
        self.id = id
        self.date = date
        self.latitude = latitude
        self.longitude = longitude
        self.depth = depth
        self.type = type
        self.magnitude = magnitude


