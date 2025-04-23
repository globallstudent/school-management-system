from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from datetime import datetime
from typing import Optional, List
from app.core.db import Base


class Exam(Base):
    __tablename__ = "exams"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String)
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)

    # Foreign keys    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"))

    lesson: Mapped["Lesson"] = relationship("Lesson", back_populates="exams")
    results: Mapped[List["Result"]] = relationship(back_populates="exam")
