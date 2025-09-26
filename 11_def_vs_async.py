import time
from fastapi import FastAPI

app = FastAPI()

@app.get("/block")
def blocking_task():
    time.sleep(5)   # blocks 5 seconds
    return {"msg": "Finished blocking"}


import asyncio

@app.get("/nonblock")
async def nonblocking_task():
    await asyncio.sleep(5)   # non-blocking wait
    return {"msg": "Finished non-blocking"}
