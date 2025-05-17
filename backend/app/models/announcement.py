from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey
from typing import Optional
from datetime import datetime
from app.database import Base

class Announcement(Base):
    __tablename__ = "announcements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    # Foreign keys
    class_id: Mapped[Optional[int]] = mapped_column(ForeignKey("classes.id"), nullable=True)

    # Relationships
    class_: Mapped[Optional["Class"]] = relationship("Class", back_populates="announcements")
