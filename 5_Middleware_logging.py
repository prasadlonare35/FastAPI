from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"📌 Request: {request.method} {request.url}")
    response = await call_next(request)
    print(f"✅ Response status: {response.status_code}")
    return response

@app.get("/items")
def get_items():
    return {"items": ["apple", "banana"]}
