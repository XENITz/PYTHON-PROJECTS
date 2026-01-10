from fastapi import FastAPI
import fastapi
import uvicorn
from pydantic import BaseModel
from typing import Optional
from .database import  engine, Base

app = fastapi.FastAPI()

## TODO: Define the data with pydantic
class SensorReadings(BaseModel):
    temperature: float
    humidity: float
    pressure: float

## TODO: Receive data
@app.post("/sensor-data/")
def receive_sensor_data(data: SensorReadings):
    return {"message": "Sensor data received", "data": data}
