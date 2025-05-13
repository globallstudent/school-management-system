<<<<<<< HEAD
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, DateTime, ForeignKey, Boolean
from datetime import datetime
=======
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship
>>>>>>> 3a65f88e582f25320a11617ef96d5593226ef1b3
from app.core.db import Base

class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, ForeignKey("students.id"), nullable=False)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False)
    present = Column(Boolean, default=True)

    student = relationship("Student", back_populates="attendances")
    lesson = relationship("Lesson", back_populates="attendances")
