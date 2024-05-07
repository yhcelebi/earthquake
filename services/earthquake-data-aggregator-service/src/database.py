# database.py

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["earthquakes"]
earthquakes_collection = db["earthquakes"]
