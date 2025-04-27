from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean, Enum
from datetime import datetime, timezone
from typing import Optional, List
from app.core.db import Base


class UserSex(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class Student(Base):
    __tablename__ = "students"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    email: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=True)
    address: Mapped[str] = mapped_column(String)
    img: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    sex: Mapped[UserSex] = mapped_column(Enum(UserSex))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )
    birthday: Mapped[datetime] = mapped_column(DateTime)

    # Foreign keys
    parent_id: Mapped[str] = mapped_column(ForeignKey("parents.id"))
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    grade_id: Mapped[int] = mapped_column(ForeignKey("grades.id"))

    # Relationships
    parent: Mapped["Parent"] = relationship("Parent", back_populates="students")
    class_: Mapped["Class"] = relationship("Class", back_populates="students")
    grade: Mapped["Grade"] = relationship("Grade", back_populates="students")
    attendances: Mapped[List["Attendance"]] = relationship(back_populates="student")
    results: Mapped[List["Result"]] = relationship(back_populates="student")
