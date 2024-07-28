from datetime import datetime, timezone
from sqlalchemy import TIMESTAMP, DateTime
from sqlalchemy.orm import Mapped, mapped_column


UTC = timezone.utc


class AbstractModel:
    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True), default=lambda: datetime.now(UTC)
    )
    last_updated: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True), default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )
    deleted_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )
