from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, Enum as SQLAEnum
from datetime import datetime, timezone
from typing import Optional, List
from enum import Enum
from app.database import Base

class DayOfWeek(str, Enum):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"

class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    day: Mapped[DayOfWeek] = mapped_column(SQLAEnum(DayOfWeek))
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)

    # Foreign keys
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    teacher_id: Mapped[str] = mapped_column(ForeignKey("teachers.id"))

    # Relationships
    subject: Mapped["Subject"] = relationship("Subject", back_populates="lessons")
    class_: Mapped["Class"] = relationship("Class", back_populates="lessons")
    teacher: Mapped["Teacher"] = relationship("Teacher", back_populates="lessons")
    exams: Mapped[List["Exam"]] = relationship(back_populates="lesson")
    assignments: Mapped[List["Assignment"]] = relationship(back_populates="lesson")
    attendances: Mapped[List["Attendance"]] = relationship(back_populates="lesson")
