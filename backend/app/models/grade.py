from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from app.core.db import Base

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    level = Column(Integer, unique=True, nullable=False)

    students = relationship("Student", back_populates="grade")
    classes = relationship("Class", back_populates="grade")
