from fastapi import FastAPI
import os
import redis

app = FastAPI()

SERVER_NAME = os.getenv("SERVER_NAME", "unknown")

redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)


@app.get("/")
def home():
    return {
        "message": "Hello from FastAPI",
        "server": SERVER_NAME
    }


@app.get("/cache/{key}")
def get_cache(key: str):
    value = redis_client.get(key)

    if value is None:
        return {
            "key": key,
            "value": None,
            "message": "Cache MISS"
        }

    return {
        "key": key,
        "value": value,
        "message": "Cache HIT"
    }


@app.post("/cache/{key}")
def set_cache(key: str, value: str):
    redis_client.set(key, value,ex=60)

    return {
        "key": key,
        "value": value,
        "message": "the data is stord for 60 sec"
    }