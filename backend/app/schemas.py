# schemas.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class UserSexEnum(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

class DayEnum(str, Enum):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"

# Base schemas for common properties
class UserBase(BaseModel):
    username: str
    name: str
    surname: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: str

# Student schemas
class StudentBase(UserBase):
    blood_type: str
    sex: UserSexEnum
    birthday: datetime

class StudentCreate(StudentBase):
    id: str
    parent_id: str
    class_id: int
    grade_id: int
    img: Optional[str] = None

class StudentResponse(StudentBase):
    id: str
    parent_id: str
    class_id: Optional[int] = None
    grade_id: int
    img: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True

# Teacher schemas
class TeacherBase(UserBase):
    blood_type: str
    sex: UserSexEnum
    birthday: datetime

class TeacherCreate(TeacherBase):
    id: str
    img: Optional[str] = None

class TeacherResponse(TeacherBase):
    id: str
    img: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True

# Parent schemas
class ParentBase(UserBase):
    pass

class ParentCreate(ParentBase):
    id: str

class ParentResponse(ParentBase):
    id: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# Class schemas
class ClassBase(BaseModel):
    name: str
    capacity: int
    grade_id: int

class ClassCreate(ClassBase):
    supervisor_id: Optional[str] = None

class ClassResponse(ClassBase):
    id: int
    supervisor_id: Optional[str] = None
    
    class Config:
        from_attributes = True

# Grade schemas
class GradeBase(BaseModel):
    level: int

class GradeCreate(GradeBase):
    pass

class GradeResponse(GradeBase):
    id: int
    
    class Config:
        from_attributes = True

# Subject schemas
class SubjectBase(BaseModel):
    name: str

class SubjectCreate(SubjectBase):
    pass

class SubjectResponse(SubjectBase):
    id: int
    
    class Config:
        from_attributes = True

# Lesson schemas
class LessonBase(BaseModel):
    name: str
    day: DayEnum
    start_time: datetime
    end_time: datetime
    subject_id: int
    class_id: int
    teacher_id: str

class LessonCreate(LessonBase):
    pass

class LessonResponse(LessonBase):
    id: int
    
    class Config:
        from_attributes = True

# Exam schemas
class ExamBase(BaseModel):
    title: str
    start_time: datetime
    end_time: datetime
    lesson_id: int

class ExamCreate(ExamBase):
    pass

class ExamResponse(ExamBase):
    id: int
    
    class Config:
        from_attributes = True

# Assignment schemas
class AssignmentBase(BaseModel):
    title: str
    start_date: datetime
    due_date: datetime
    lesson_id: int

class AssignmentCreate(AssignmentBase):
    pass

class AssignmentResponse(AssignmentBase):
    id: int
    
    class Config:
        from_attributes = True

# Result schemas
class ResultBase(BaseModel):
    score: int
    student_id: str
    exam_id: Optional[int] = None
    assignment_id: Optional[int] = None

class ResultCreate(ResultBase):
    pass

class ResultResponse(ResultBase):
    id: int
    
    class Config:
        from_attributes = True

# Attendance schemas
class AttendanceBase(BaseModel):
    date: datetime
    present: bool
    student_id: str
    lesson_id: int

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceResponse(AttendanceBase):
    id: int
    
    class Config:
        from_attributes = True

# Event schemas
class EventBase(BaseModel):
    title: str
    description: str
    start_time: datetime
    end_time: datetime
    class_id: Optional[int] = None

class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    id: int
    
    class Config:
        from_attributes = True

# Announcement schemas
class AnnouncementBase(BaseModel):
    title: str
    description: str
    date: datetime
    class_id: Optional[int] = None

class AnnouncementCreate(AnnouncementBase):
    pass

class AnnouncementResponse(AnnouncementBase):
    id: int
    
    class Config:
        from_attributes = True
