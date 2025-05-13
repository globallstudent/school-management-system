from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey
from datetime import datetime
from typing import List
from app.core.db import Base


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    day: Mapped[Day] = mapped_column(SQLAEnum(Day))
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)

    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    teacher_id: Mapped[str] = mapped_column(ForeignKey("teachers.id"))

    subject: Mapped["Subject"] = relationship("Subject", back_populates="lessons")
    class_: Mapped["Class"] = relationship("Class", back_populates="lessons")
    teacher: Mapped["Teacher"] = relationship("Teacher", back_populates="lessons")
    exams: Mapped[List["Exam"]] = relationship(back_populates="lesson")
    assignments: Mapped[List["Assignment"]] = relationship(back_populates="lesson")
    attendances: Mapped[List["Attendance"]] = relationship(back_populates="lesson")
