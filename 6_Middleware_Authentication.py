from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.middleware("http")
async def auth_middleware(request:Request, call_next):
    token  = request.headers.get("Authorization")
    if token != "secret123":
        return JSONResponse({"error":"Unauthorized"}, status_code=401)
    
    return await call_next(request)

@app.get("/secure-data")
def secure_data():
    return {"message": "You have access ✅"}