from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from datetime import datetime
from typing import Optional, List
from app.core.db import Base


class Grade(Base):
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    level: Mapped[int] = mapped_column(Integer, unique=True)

    # Relationships
    students: Mapped[List["Student"]] = relationship(back_populates="grade")
    classes: Mapped[List["Class"]] = relationship(back_populates="grade")
