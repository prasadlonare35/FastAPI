from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

@app.get("/task")
def run_task(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "User visited /task")
    return {"message": "Task started!"}

@app.get("/")
def run_task(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "User visited /")
    return {"message": "Task started!"}