from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey
from datetime import datetime
from typing import Optional
from app.core.db import Base


class Announcement(Base):
    __tablename__ = "announcements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    date: Mapped[datetime] = mapped_column(DateTime)

    class_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("classes.id"), nullable=True
    )

    class_: Mapped[Optional["Class"]] = relationship(
        "Class", back_populates="announcements"
    )
