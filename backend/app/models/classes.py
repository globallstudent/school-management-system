from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from typing import Optional, List
from app.database import Base

class Class(Base):
    __tablename__ = "classes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    capacity: Mapped[int] = mapped_column(Integer)

    # Foreign keys
    supervisor_id: Mapped[Optional[str]] = mapped_column(ForeignKey("teachers.id"), nullable=True)
    grade_id: Mapped[int] = mapped_column(ForeignKey("grades.id"))

    # Relationships
    supervisor: Mapped[Optional["Teacher"]] = relationship("Teacher", back_populates="supervised_classes")
    grade: Mapped["Grade"] = relationship("Grade", back_populates="classes")
    lessons: Mapped[List["Lesson"]] = relationship(back_populates="class_")
    students: Mapped[List["Student"]] = relationship(back_populates="class_")
    events: Mapped[List["Event"]] = relationship(back_populates="class_")
    announcements: Mapped[List["Announcement"]] = relationship(back_populates="class_")
