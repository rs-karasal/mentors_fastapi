from pydantic import BaseModel
from datetime import datetime


class Message(BaseModel):
    chat_id: int
    sender: str
    content: str
    timestamp: datetime = datetime.now()
