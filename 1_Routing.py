from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{
        "message" : "HomePage"
    }
    
@app.get("/hello")
def greet():
    return{
        "message" : "Hello Prasad, How are You?",
        "name":"Prasad",
        "age":21
    }
