from fastapi import APIRouter, WebSocket, WebSocketDisconnect
router = APIRouter()
active_connections = {}
@router.websocket("/ws/{user_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    user_id: int
):
    await websocket.accept()
    active_connections[user_id] = websocket
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(
                f"Message received: {data}"
            )
    except WebSocketDisconnect:
        del active_connections[user_id]