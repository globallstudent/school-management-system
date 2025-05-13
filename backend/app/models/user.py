from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.db import Base
import enum

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    STUDENT = "student"
    TEACHER = "teacher"
    PARENT = "parent"

class UserSex(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=True)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    sex = Column(Enum(UserSex), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    student = relationship("Student", back_populates="user", uselist=False)
    teacher = relationship("Teacher", back_populates="user", uselist=False)
    parent = relationship("Parent", back_populates="user", uselist=False)
    admin = relationship("Admin", back_populates="user", uselist=False)
