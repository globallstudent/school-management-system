from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from app.models.user import UserRole
from app.models.user import UserSex


class UserBase(BaseModel):
    """Base schema for user data"""
    username: str
    email: Optional[EmailStr] = None


class UserCreate(UserBase):
    """Schema for creating a user"""
    password: str
    id: Optional[str] = None


class UserResponse(UserBase):
    """Schema for user response"""
    id: str
    role: UserRole
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True


class UserInDB(UserResponse):
    """Schema for user in database"""
    hashed_password: str

    class Config:
        orm_mode = True


class AdminBase(BaseModel):
    """Base schema for admin data"""
    username: str


class AdminCreate(UserCreate, AdminBase):
    """Schema for creating an admin"""
    pass


class TeacherBase(BaseModel):
    """Base schema for teacher data"""
    name: str
    surname: str
    address: str
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    img: Optional[str] = None
    blood_type: Optional[str] = None
    sex: UserSex
    birthday: datetime


class TeacherCreate(UserCreate, TeacherBase):
    """Schema for creating a teacher"""
    pass


class StudentBase(BaseModel):
    """Base schema for student data"""
    name: str
    surname: str
    address: str
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    img: Optional[str] = None
    blood_type: str
    sex: UserSex
    birthday: datetime
    parent_id: str
    class_id: int
    grade_id: int


class StudentCreate(UserCreate, StudentBase):
    """Schema for creating a student"""
    pass


class ParentBase(BaseModel):
    """Base schema for parent data"""
    name: str
    surname: str
    address: str
    phone: str
    email: Optional[EmailStr] = None


class ParentCreate(UserCreate, ParentBase):
    """Schema for creating a parent"""
    pass
