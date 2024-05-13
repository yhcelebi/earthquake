# database.py

from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_COLLECTION = os.getenv("DB_COLLECTION")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

client = MongoClient(f"mongodb://{DB_USERNAME}:{DB_PASSWORD}@localhost:27017/")
db = client[DB_NAME]
earthquakes_collection = db[DB_COLLECTION]
