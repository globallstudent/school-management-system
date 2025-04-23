from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from datetime import datetime
from typing import Optional, List
from app.core.db import Base


class Class(Base):
    __tablename__ = "classes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    capacity: Mapped[int] = mapped_column(Integer)

    # Foreign keys
    supervisor_id: Mapped[Optional[str]] = mapped_column(
        ForeignKey("teachers.id"), nullable=True
    )
    grade_id: Mapped[int] = mapped_column(ForeignKey("grades.id"))

    # Relationships
    supervisor: Mapped[Optional["Teacher"]] = relationship(
        "Teacher", back_populates="supervised_classes"
    )
    lessons: Mapped[List["Lesson"]] = relationship(back_populates="class_")
    students: Mapped[List["Student"]] = relationship(back_populates="class_")
    grade: Mapped["Grade"] = relationship(back_populates="classes")
    events: Mapped[List["Event"]] = relationship(back_populates="class_")
    announcements: Mapped[List["Announcement"]] = relationship(back_populates="class_")
