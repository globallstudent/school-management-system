<<<<<<< HEAD
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey, Enum
from datetime import datetime, timezone
from typing import Optional, List
=======
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from datetime import datetime
>>>>>>> 3a65f88e582f25320a11617ef96d5593226ef1b3
from app.core.db import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(String, ForeignKey("users.id"), primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=True)
    email = Column(String, unique=True, nullable=True)
    img = Column(String, nullable=True)
    birthday = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    parent_id = Column(String, ForeignKey("parents.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    grade_id = Column(Integer, ForeignKey("grades.id"), nullable=False)

    user = relationship("User", back_populates="student")
    parent = relationship("Parent", back_populates="students")
    class_ = relationship("Class", back_populates="students")
    grade = relationship("Grade", back_populates="students")

    attendances = relationship("Attendance", back_populates="student")
    results = relationship("Result", back_populates="student")
