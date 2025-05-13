<<<<<<< HEAD
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from typing import Optional, List
=======
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
>>>>>>> 3a65f88e582f25320a11617ef96d5593226ef1b3
from app.core.db import Base

class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    capacity = Column(Integer, nullable=False)

    supervisor_id = Column(String, ForeignKey("teachers.id"), nullable=True)
    grade_id = Column(Integer, ForeignKey("grades.id"), nullable=False)

    supervisor = relationship("Teacher", back_populates="classes")
    grade = relationship("Grade", back_populates="classes")

    lessons = relationship("Lesson", back_populates="class_")
    students = relationship("Student", back_populates="class_")
    events = relationship("Event", back_populates="class_")
    announcements = relationship("Announcement", back_populates="class_")
