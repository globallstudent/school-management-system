from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey, Integer
from datetime import datetime, timezone
from typing import Optional, List
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), primary_key=True)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)
    phone: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=True)
    img: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    birthday: Mapped[datetime] = mapped_column(DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    parent_id: Mapped[str] = mapped_column(String, ForeignKey("parents.id"))
    class_id: Mapped[int] = mapped_column(Integer, ForeignKey("classes.id"))
    grade_id: Mapped[int] = mapped_column(Integer, ForeignKey("grades.id"))

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="student")
    parent: Mapped["Parent"] = relationship("Parent", back_populates="students")
    class_: Mapped["Class"] = relationship("Class", back_populates="students")
    grade: Mapped["Grade"] = relationship("Grade", back_populates="students")
    attendances: Mapped[List["Attendance"]] = relationship(back_populates="student")
    results: Mapped[List["Result"]] = relationship(back_populates="student")
