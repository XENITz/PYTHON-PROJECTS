from fastapi import FastAPI
import time
import asyncio

app =  FastAPI()

@app.get("/")
async def root():
  