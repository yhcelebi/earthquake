from pymongo import MongoClient

username = "rootuser"
password = "rootpass"
database_name = "earthquakes"

client = MongoClient(f"mongodb://{username}:{password}@localhost:27017/")
db = client[database_name]
earthquakes_collection = db["earthquakes"]
