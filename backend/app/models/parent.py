<<<<<<< HEAD
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime
=======
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
>>>>>>> 3a65f88e582f25320a11617ef96d5593226ef1b3
from datetime import datetime
from app.core.db import Base

class Parent(Base):
    __tablename__ = "parents"

    id = Column(String, ForeignKey("users.id"), primary_key=True)
    address = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="parent")
    students = relationship("Student", back_populates="parent")
