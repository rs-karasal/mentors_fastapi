from datetime import datetime, UTC
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String, TIMESTAMP, Boolean, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.abstracts.models import AbstractModel
from src.database import Base


class AccountType(Base):
    """
    There are different types of accounts, each with different permissions.
    For example: mentee (only learn), mentor (learn and teach), admin (manage mentees and mentors).
    """
    __tablename__ = "account_type"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=100), nullable=False)
    permissions: Mapped[str] = mapped_column(String(length=100), nullable=False)

    users = relationship("User", back_populates="account_type")


class User(SQLAlchemyBaseUserTable[int], Base, AbstractModel):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(length=100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(length=100), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    registered_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=False, default=datetime.now(UTC))
    account_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("account_type.id"), nullable=False, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    account_type = relationship("AccountType", back_populates="users")
