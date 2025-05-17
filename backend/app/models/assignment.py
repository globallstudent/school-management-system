from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey
from datetime import datetime, timezone
from typing import Optional, List
from app.database import Base

class Assignment(Base):
    __tablename__ = "assignments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    start_date: Mapped[datetime] = mapped_column(DateTime)
    due_date: Mapped[datetime] = mapped_column(DateTime)
    
    # Foreign keys
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"))
    
    # Relationships
    lesson: Mapped["Lesson"] = relationship("Lesson", back_populates="assignments")
    results: Mapped[List["Result"]] = relationship(back_populates="assignment")
