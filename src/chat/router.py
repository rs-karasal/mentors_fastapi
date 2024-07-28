import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from fastapi_users import FastAPIUsers
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from src.auth.manager import get_user_manager
from src.auth.auth import get_jwt_strategy
from src.database import get_async_session
from src.chat.schemas import MessageCreate
from src.chat.manager import ConnectionManager

router = APIRouter()


manager = ConnectionManager()


fastapi_users = FastAPIUsers[User, int](get_user_manager, [get_jwt_strategy()])


@router.websocket("/ws/chat/{chat_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    chat_id: str,
    user: User = Depends(fastapi_users.current_user()),
    db: AsyncSession = Depends(get_async_session)
):
    await manager.connect(websocket, chat_id, user)
    try:
        while True:
            data = await websocket.receive_json()
            message_data = MessageCreate(
                chat_id=int(chat_id),
                from_user=user.id,
                text=data.get("text")
            )
            await manager.save_message(db, message_data)
            await manager.broadcast(message_data.text, chat_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket, chat_id)
        await manager.broadcast(json.dumps({"message": "Client disconnected"}), chat_id)
