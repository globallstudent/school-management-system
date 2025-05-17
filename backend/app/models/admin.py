from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.database import Base

class Admin(Base):
    __tablename__ = "admins"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    
    # Relationships
    user: Mapped["User"] = relationship("User")
