from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Hello! You are connected 🚀")
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"You said: {data}")
