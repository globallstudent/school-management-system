<<<<<<< HEAD
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey
from datetime import datetime
from typing import List
=======
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
>>>>>>> 3a65f88e582f25320a11617ef96d5593226ef1b3
from app.core.db import Base
import enum

class DayOfWeek(str, enum.Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    day = Column(Enum(DayOfWeek), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    teacher_id = Column(String, ForeignKey("teachers.id"), nullable=False)

    subject = relationship("Subject", back_populates="lessons")
    class_ = relationship("Class", back_populates="lessons")
    teacher = relationship("Teacher", back_populates="lessons")

    exams = relationship("Exam", back_populates="lesson")
    assignments = relationship("Assignment", back_populates="lesson")
    attendances = relationship("Attendance", back_populates="lesson")
