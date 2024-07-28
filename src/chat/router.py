import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.chat.schemas import MessageCreate
from src.chat.manager import ConnectionManager

router = APIRouter()


manager = ConnectionManager()


@router.websocket("/ws/chat/{chat_id}")
async def websocket_endpoint(
    websocket: WebSocket, chat_id: str, db: AsyncSession = Depends(get_async_session)
):
    await manager.connect(websocket, chat_id)
    try:
        while True:
            data = await websocket.receive_json()
            message_data = MessageCreate(
                chat_id=int(chat_id),
                from_user=data.get("from_user"),
                text=data.get("text")
            )
            await manager.save_message(db, message_data)
            await manager.broadcast(message_data.text, chat_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket, chat_id)
        await manager.broadcast(json.dumps({"message": "Client disconnected"}), chat_id)
