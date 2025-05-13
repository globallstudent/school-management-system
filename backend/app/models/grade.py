<<<<<<< HEAD
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer
from typing import List
=======
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
>>>>>>> 3a65f88e582f25320a11617ef96d5593226ef1b3
from app.core.db import Base

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    level = Column(Integer, unique=True, nullable=False)

    students = relationship("Student", back_populates="grade")
    classes = relationship("Class", back_populates="grade")
