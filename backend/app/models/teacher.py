from sqlalchemy import String, DateTime, ForeignKey, Table, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone
from typing import Optional, List
from app.database import Base

# Association Table for Teacher-Subject Many-to-Many
teacher_subject = Table(
    "teacher_subject",
    Base.metadata,
    Column("teacher_id", String, ForeignKey("teachers.id"), primary_key=True),
    Column("subject_id", Integer, ForeignKey("subjects.id"), primary_key=True),
)

class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), primary_key=True)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)
    phone: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=True)
    img: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    birthday: Mapped[datetime] = mapped_column(DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="teacher")
    subjects: Mapped[List["Subject"]] = relationship(secondary=teacher_subject, back_populates="teachers")
    lessons: Mapped[List["Lesson"]] = relationship(back_populates="teacher")
    supervised_classes: Mapped[List["Class"]] = relationship(back_populates="supervisor")
