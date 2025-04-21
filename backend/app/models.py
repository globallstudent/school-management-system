# models.py
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, DateTime, Integer, Boolean, ForeignKey, Enum as SQLAEnum, Table, Column
from datetime import datetime, timezone
from typing import Optional, List
from enum import Enum
from app.database import Base

class UserSex(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

class Day(str, Enum):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"

# Association table for many-to-many relationship between Teacher and Subject
teacher_subject = Table(
    "teacher_subject",
    Base.metadata,
    Column("teacher_id", String, ForeignKey("teachers.id"), primary_key=True),
    Column("subject_id", Integer, ForeignKey("subjects.id"), primary_key=True)
)

class Admin(Base):
    __tablename__ = "admins"
    
    id: Mapped[str] = mapped_column(String, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)

class Parent(Base):
    __tablename__ = "parents"
    
    id: Mapped[str] = mapped_column(String, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    email: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=True)
    phone: Mapped[str] = mapped_column(String, unique=True)
    address: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    # Relationships
    students: Mapped[List["Student"]] = relationship(back_populates="parent")

class Grade(Base):
    __tablename__ = "grades"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    level: Mapped[int] = mapped_column(Integer, unique=True)
    
    # Relationships
    students: Mapped[List["Student"]] = relationship(back_populates="grade")
    classes: Mapped[List["Class"]] = relationship(back_populates="grade")

class Teacher(Base):
    __tablename__ = "teachers"
    
    id: Mapped[str] = mapped_column(String, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    email: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=True)
    address: Mapped[str] = mapped_column(String)
    img: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    blood_type: Mapped[str] = mapped_column(String)
    sex: Mapped[UserSex] = mapped_column(SQLAEnum(UserSex))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    birthday: Mapped[datetime] = mapped_column(DateTime)
    
    # Relationships
    subjects: Mapped[List["Subject"]] = relationship(secondary=teacher_subject, back_populates="teachers")
    lessons: Mapped[List["Lesson"]] = relationship(back_populates="teacher")
    supervised_classes: Mapped[List["Class"]] = relationship(back_populates="supervisor")

class Class(Base):
    __tablename__ = "classes"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    capacity: Mapped[int] = mapped_column(Integer)
    
    # Foreign keys
    supervisor_id: Mapped[Optional[str]] = mapped_column(ForeignKey("teachers.id"), nullable=True)
    grade_id: Mapped[int] = mapped_column(ForeignKey("grades.id"))
    
    # Relationships
    supervisor: Mapped[Optional["Teacher"]] = relationship("Teacher", back_populates="supervised_classes")
    lessons: Mapped[List["Lesson"]] = relationship(back_populates="class_")
    students: Mapped[List["Student"]] = relationship(back_populates="class_")
    grade: Mapped["Grade"] = relationship(back_populates="classes")
    events: Mapped[List["Event"]] = relationship(back_populates="class_")
    announcements: Mapped[List["Announcement"]] = relationship(back_populates="class_")

class Student(Base):
    __tablename__ = "students"
    
    id: Mapped[str] = mapped_column(String, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    email: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=True)
    address: Mapped[str] = mapped_column(String)
    img: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    blood_type: Mapped[str] = mapped_column(String)
    sex: Mapped[UserSex] = mapped_column(SQLAEnum(UserSex))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
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

class Subject(Base):
    __tablename__ = "subjects"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    
    # Relationships
    teachers: Mapped[List["Teacher"]] = relationship(secondary=teacher_subject, back_populates="subjects")
    lessons: Mapped[List["Lesson"]] = relationship(back_populates="subject")

class Lesson(Base):
    __tablename__ = "lessons"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    day: Mapped[Day] = mapped_column(SQLAEnum(Day))
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)
    
    # Foreign keys
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    teacher_id: Mapped[str] = mapped_column(ForeignKey("teachers.id"))
    
    # Relationships
    subject: Mapped["Subject"] = relationship("Subject", back_populates="lessons")
    class_: Mapped["Class"] = relationship("Class", back_populates="lessons")
    teacher: Mapped["Teacher"] = relationship("Teacher", back_populates="lessons")
    exams: Mapped[List["Exam"]] = relationship(back_populates="lesson")
    assignments: Mapped[List["Assignment"]] = relationship(back_populates="lesson")
    attendances: Mapped[List["Attendance"]] = relationship(back_populates="lesson")

class Exam(Base):
    __tablename__ = "exams"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String)
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)
    
    # Foreign keys
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"))
    
    # Relationships
    lesson: Mapped["Lesson"] = relationship("Lesson", back_populates="exams")
    results: Mapped[List["Result"]] = relationship(back_populates="exam")

class Assignment(Base):
    __tablename__ = "assignments"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String)
    start_date: Mapped[datetime] = mapped_column(DateTime)
    due_date: Mapped[datetime] = mapped_column(DateTime)
    
    # Foreign keys
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"))
    
    # Relationships
    lesson: Mapped["Lesson"] = relationship("Lesson", back_populates="assignments")
    results: Mapped[List["Result"]] = relationship(back_populates="assignment")

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

class Attendance(Base):
    __tablename__ = "attendances"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date: Mapped[datetime] = mapped_column(DateTime)
    present: Mapped[bool] = mapped_column(Boolean)
    
    # Foreign keys
    student_id: Mapped[str] = mapped_column(ForeignKey("students.id"))
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"))
    
    # Relationships
    student: Mapped["Student"] = relationship("Student", back_populates="attendances")
    lesson: Mapped["Lesson"] = relationship("Lesson", back_populates="attendances")

class Event(Base):
    __tablename__ = "events"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)
    
    # Foreign keys
    class_id: Mapped[Optional[int]] = mapped_column(ForeignKey("classes.id"), nullable=True)
    
    # Relationships
    class_: Mapped[Optional["Class"]] = relationship("Class", back_populates="events")

class Announcement(Base):
    __tablename__ = "announcements"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    date: Mapped[datetime] = mapped_column(DateTime)
    
    # Foreign keys
    class_id: Mapped[Optional[int]] = mapped_column(ForeignKey("classes.id"), nullable=True)
    
    # Relationships
    class_: Mapped[Optional["Class"]] = relationship("Class", back_populates="announcements")