import datetime

from sqlalchemy import (
    Boolean,
    Column,   
    ForeignKey, 
    Integer,
    JSON,
    MetaData,
    String,
    Table,
    TIMESTAMP
    )


metadata = MetaData()


role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON)
)


user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False, unique=True),
    Column("full_name", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.datetime.utcnow, nullable=False),
    Column("role_id", Integer, ForeignKey(role.c.id), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)
