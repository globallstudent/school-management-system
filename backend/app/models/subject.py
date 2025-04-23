from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean, Table, Column
from datetime import datetime
from typing import Optional, List
from app.core.db import Base

teacher_subject = Table(
    "teacher_subject",
    Base.metadata,
    Column("teacher_id", String, ForeignKey("teachers.id"), primary_key=True),
    Column("subject_id", Integer, ForeignKey("subjects.id"), primary_key=True),
)


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    # Relationships
    teachers: Mapped[List["Teacher"]] = relationship(
        secondary=teacher_subject, back_populates="subjects"
    )
    lessons: Mapped[List["Lesson"]] = relationship(back_populates="subject")
