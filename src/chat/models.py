from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.abstracts.models import AbstractModel
from src.database import Base


class Chat(Base, AbstractModel):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    messages = relationship("Message", back_populates="chat")
    chat_member = relationship("User", back_populates="chat")


class Message(Base, AbstractModel):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    chat_id: Mapped[int] = mapped_column(Integer, ForeignKey("chats.id"), nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=False)
    from_user: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)

    chat = relationship("Chat", back_populates="messages")
    # user = relationship("User", back_populates="messages")


class ChatMember(Base):
    __tablename__ = "chat_members"

    chat_id: Mapped[int] = mapped_column(Integer, ForeignKey("chats.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)

    chat = relationship("Chat", back_populates="chat_member")
    # user = relationship("User", back_populates="chat_member")
