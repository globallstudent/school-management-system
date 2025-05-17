from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey
from datetime import datetime, timezone
from typing import Optional, List
from app.database import Base

class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)
    class_id: Mapped[Optional[int]] = mapped_column(ForeignKey("classes.id"), nullable=True)
    
    # Relationships
    class_: Mapped[Optional["Class"]] = relationship("Class", back_populates="events")
