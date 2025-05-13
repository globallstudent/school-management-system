<<<<<<< HEAD
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey
from datetime import datetime
from typing import Optional
=======
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
>>>>>>> 3a65f88e582f25320a11617ef96d5593226ef1b3
from app.core.db import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    date = Column(DateTime, nullable=False)

    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)

    class_ = relationship("Class", back_populates="events")
