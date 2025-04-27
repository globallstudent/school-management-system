from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
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
