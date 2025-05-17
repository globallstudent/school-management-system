from sqlalchemy import String, DateTime, Boolean, Enum as SQLAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone
from typing import Optional, List
from enum import Enum
from app.database import Base

class UserRole(str, Enum):
    ADMIN = "ADMIN"
    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    PARENT = "PARENT"

class UserSex(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=True)
    hashed_password: Mapped[str] = mapped_column(String)
    role: Mapped[UserRole] = mapped_column(SQLAEnum(UserRole))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )

    # Relationships
    student = relationship("Student", back_populates="user", uselist=False)
    teacher = relationship("Teacher", back_populates="user", uselist=False)
    parent = relationship("Parent", back_populates="user", uselist=False)
    admin = relationship("Admin", back_populates="user", uselist=False)
