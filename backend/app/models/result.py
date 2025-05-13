<<<<<<< HEAD
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey
from typing import Optional
=======
from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship
>>>>>>> 3a65f88e582f25320a11617ef96d5593226ef1b3
from app.core.db import Base

class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, ForeignKey("students.id"), nullable=False)
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False)
    score = Column(Float, nullable=False)

    student = relationship("Student", back_populates="results")
    exam = relationship("Exam")
