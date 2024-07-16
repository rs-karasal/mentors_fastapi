from datetime import datetime, UTC
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column


class AbstractModel:
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=datetime.now(UTC))
    last_updated: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP, default=datetime.now(UTC), onupdate=datetime.now(UTC)
    )
    deleted_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=True)
