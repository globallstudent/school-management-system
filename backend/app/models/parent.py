from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey
from datetime import datetime, timezone
from typing import Optional, List
from app.database import Base

class Parent(Base):
    __tablename__ = "parents"

    id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), primary_key=True)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="parent")
    students: Mapped[List["Student"]] = relationship(back_populates="parent")
