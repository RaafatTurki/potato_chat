from fastapi import WebSocket
from fastapi.responses import HTMLResponse

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self,WebSocket:WebSocket):
        await WebSocket.accept()
        self.active_connections.append(WebSocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
