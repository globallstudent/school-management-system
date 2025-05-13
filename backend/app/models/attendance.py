from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, DateTime, ForeignKey, Boolean
from datetime import datetime
from app.core.db import Base


class Attendance(Base):
    __tablename__ = "attendances"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date: Mapped[datetime] = mapped_column(DateTime)
    present: Mapped[bool] = mapped_column(Boolean)

    # Foreign keys
    student_id: Mapped[str] = mapped_column(ForeignKey("students.id"))
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"))

    # Relationships
    student: Mapped["Student"] = relationship("Student", back_populates="attendances")
    lesson: Mapped["Lesson"] = relationship("Lesson", back_populates="attendances")
