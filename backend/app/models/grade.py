from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer
from typing import List
from app.database import Base

class Grade(Base):
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    level: Mapped[int] = mapped_column(Integer, unique=True)

    # Relationships
    students: Mapped[List["Student"]] = relationship(back_populates="grade")
    classes: Mapped[List["Class"]] = relationship(back_populates="grade")
