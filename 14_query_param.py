from fastapi import FastAPI, Query, HTTPException
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

@app.get("/sort")
def sort(sort_by:str = Query(...,description="Sorting by Height, weight, bmi"), order:str = Query('asc', description="sort by asc or desc")):
    data = load_data()
    valid = ['height','weight','bmi']
    if sort_by not in valid:
        raise HTTPException(status_code=400,detail="BAD REQUEST")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail="BAD REQUEST")
    
    sort_order = True if order == 'desc' else False
    
    sorted_data  = sorted(data.values(), key = lambda x : x.get(sort_by,0), reverse=sort_order)
    return sorted_data