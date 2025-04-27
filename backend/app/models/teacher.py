from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean, Enum, Table, Column
from datetime import datetime, timezone
from typing import Optional, List
from app.core.db import Base

class UserSex(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

teacher_subject = Table(
    "teacher_subject",
    Base.metadata,
    Column("teacher_id", String, ForeignKey("teachers.id"), primary_key=True),
    Column("subject_id", Integer, ForeignKey("subjects.id"), primary_key=True),
)

class Teacher(Base):
    __tablename__ = "teachers"

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

    # Relationships
    subjects: Mapped[List["Subject"]] = relationship(
        secondary=teacher_subject, back_populates="teachers"
    )
    lessons: Mapped[List["Lesson"]] = relationship(back_populates="teacher")
    supervised_classes: Mapped[List["Class"]] = relationship(
        back_populates="supervisor"
    )