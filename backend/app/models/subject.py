<<<<<<< HEAD
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Table, Column
from typing import List
=======
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
>>>>>>> 3a65f88e582f25320a11617ef96d5593226ef1b3
from app.core.db import Base
from .teacher import teacher_subject

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    teachers = relationship("Teacher", secondary=teacher_subject, back_populates="subjects")
    lessons = relationship("Lesson", back_populates="subject")
