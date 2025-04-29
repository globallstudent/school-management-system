from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.db import Base

class Admin(Base):
    __tablename__ = "admins"

    id = Column(String, ForeignKey("users.id"), primary_key=True)
    user = relationship("User", back_populates="admin")
