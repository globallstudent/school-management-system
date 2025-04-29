from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
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
