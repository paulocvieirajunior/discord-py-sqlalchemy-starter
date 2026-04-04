from .base import Base

from sqlalchemy import func, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

class User(Base):
    id: Mapped[str] = mapped_column(primary_key=True)
    coins: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
