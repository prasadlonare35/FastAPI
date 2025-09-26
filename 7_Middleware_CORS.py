from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend (React/Angular/JS) to talk to API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data")
def get_data():
    return {"message": "CORS Example"}
