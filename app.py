from fastapi import FastAPI
import os

app = FastAPI()

SERVER_NAME = os.getenv("SERVER_NAME", "unknown")


@app.get("/")
def home():
    return {
        "message": "Hello from FastAPI",
        "server": SERVER_NAME
    }