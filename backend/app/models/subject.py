from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from typing import List
from app.database import Base
from .teacher import teacher_subject

class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    # Relationships
    teachers: Mapped[List["Teacher"]] = relationship(secondary=teacher_subject, back_populates="subjects")
    lessons: Mapped[List["Lesson"]] = relationship(back_populates="subject")
