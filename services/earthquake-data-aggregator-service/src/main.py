# main.py

from database import earthquakes_collection
from models import Earthquake, EarthquakeCreate
from uuid import uuid4
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

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


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Message: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("A client disconnected.")


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
