<<<<<<< HEAD
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
=======
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
>>>>>>> 3a65f88e582f25320a11617ef96d5593226ef1b3
from app.core.db import Base

class Admin(Base):
    __tablename__ = "admins"

    id = Column(String, ForeignKey("users.id"), primary_key=True)
    user = relationship("User", back_populates="admin")
