from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Float, ForeignKey, String
from typing import Optional
from app.database import Base

class Result(Base):
    __tablename__ = "results"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    score: Mapped[int] = mapped_column(Integer)
    
    # Foreign keys
    exam_id: Mapped[Optional[int]] = mapped_column(ForeignKey("exams.id"), nullable=True)
    assignment_id: Mapped[Optional[int]] = mapped_column(ForeignKey("assignments.id"), nullable=True)
    student_id: Mapped[str] = mapped_column(ForeignKey("students.id"))
    
    # Relationships
    exam: Mapped[Optional["Exam"]] = relationship("Exam", back_populates="results")
    assignment: Mapped[Optional["Assignment"]] = relationship("Assignment", back_populates="results")
    student: Mapped["Student"] = relationship("Student", back_populates="results")
