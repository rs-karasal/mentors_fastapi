from pydantic import BaseModel
from datetime import datetime


class MessageBase(BaseModel):
    chat_id: int
    from_user: int
    text: str

    class Config:
        from_attributes = True


class MessageCreate(MessageBase):
    pass


class MessageInDB(MessageBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
