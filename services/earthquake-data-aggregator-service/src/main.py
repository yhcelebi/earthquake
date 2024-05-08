# main.py

from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from typing import List
from database import earthquakes_collection
from models import Earthquake, EarthquakeCreate
from uuid import uuid4


app = FastAPI()


@app.get("/")
async def root():
    response = await root()

    # Check the status code of the response
    if response.status_code == 200:
        print("Response status: 200 OK")
    else:
        print("Response status:", response.status_code)

    # Check the content of the response
    print("Response content:", response.content)


@app.get("/earthquakes/", response_model=List[Earthquake])
async def read_earthquakes():
    # Retrieve all earthquakes from the collection
    return await earthquakes_collection.find().to_list(length=None)


@app.post("/earthquakes/", response_model=Earthquake)
async def create_earthquake(earthquake: EarthquakeCreate):
    # Generate a UUID for the new earthquake
    earthquake_id = uuid4()

    # Insert a new earthquake into the collection with the generated UUID
    new_earthquake = earthquakes_collection.insert_one({**earthquake.dict(), "id": str(earthquake_id)})

    # Return the newly created earthquake
    return earthquakes_collection.find_one({"_id": new_earthquake.inserted_id})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
