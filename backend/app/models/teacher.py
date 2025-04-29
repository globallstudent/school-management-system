from sqlalchemy import Column, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.db import Base

# Association Table for Teacher-Subject Many-to-Many
teacher_subject = Table(
    "teacher_subject",
    Base.metadata,
    Column("teacher_id", String, ForeignKey("teachers.id")),
    Column("subject_id", ForeignKey("subjects.id"))
)

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(String, ForeignKey("users.id"), primary_key=True)
    address = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=True)
    img = Column(String, nullable=True)
    birthday = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="teacher")
    subjects = relationship("Subject", secondary=teacher_subject, back_populates="teachers")
    lessons = relationship("Lesson", back_populates="teacher")
    classes = relationship("Class", back_populates="supervisor")
