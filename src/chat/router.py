import json
from datetime import datetime

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from src.chat.models import Message
from src.chat.manager import ConnectionManager

router = APIRouter()


manager = ConnectionManager()


@router.websocket("/ws/chat/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: str):
    await manager.connect(websocket, chat_id)
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            message = Message(
                chat_id=chat_id,
                sender=message_data["sender"],
                content=message_data["content"],
                timestamp=datetime.now()
            )
            await manager.broadcast(message.json(), chat_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket, chat_id)
        await manager.broadcast(json.dumps({"message": "Client disconnected"}), chat_id)
