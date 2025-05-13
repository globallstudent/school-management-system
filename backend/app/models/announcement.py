from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.db import Base

class Announcement(Base):
    __tablename__ = "announcements"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)

    class_ = relationship("Class", back_populates="announcements")
