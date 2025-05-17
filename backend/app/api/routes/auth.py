from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import uuid

from app.core.deps import get_db, get_current_admin
from app.core.security import (
    create_access_token,
    get_password_hash,
    verify_password,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from app.models import User, Admin, Teacher, Student, Parent, UserRole
from app.schemas import (
    Token,
    UserCreate,
    UserResponse,
    AdminCreate,
    TeacherCreate,
    StudentCreate,
    ParentCreate,
)

router = APIRouter()


@router.post("/login", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    # Find the user by username
    result = await db.execute(select(User).filter(User.username == form_data.username))
    user = result.scalars().first()
    
    # Check if user exists and password is correct
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Check if user is active
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user",
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "role": user.role},
        expires_delta=access_token_expires,
    )
    
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/admin/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_admin(
    admin_in: AdminCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_admin),
) -> Any:
    """
    Register a new admin (only admins can register other admins)
    """
    # Check if username already exists
    result = await db.execute(select(User).filter(User.username == admin_in.username))
    if result.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    
    # Create new user with admin role
    user_id = admin_in.id if admin_in.id else str(uuid.uuid4())
    user = User(
        id=user_id,
        username=admin_in.username,
        hashed_password=get_password_hash(admin_in.password),
        role=UserRole.ADMIN,
    )
    db.add(user)
    
    # Create admin record
    admin = Admin(
        id=user_id,
        username=admin_in.username,
        user_id=user.id,
    )
    db.add(admin)
    
    await db.commit()
    await db.refresh(user)
    
    return user


@router.post("/teacher/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_teacher(
    teacher_in: TeacherCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_admin),
) -> Any:
    """
    Register a new teacher (only admins can register teachers)
    """
    # Check if username already exists
    result = await db.execute(select(User).filter(User.username == teacher_in.username))
    if result.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    
    # Create new user with teacher role
    user_id = teacher_in.id if teacher_in.id else str(uuid.uuid4())
    user = User(
        id=user_id,
        username=teacher_in.username,
        email=teacher_in.email,
        hashed_password=get_password_hash(teacher_in.password),
        role=UserRole.TEACHER,
    )
    db.add(user)
    
    # Create teacher record
    teacher = Teacher(
        id=user_id,
        username=teacher_in.username,
        name=teacher_in.name,
        surname=teacher_in.surname,
        email=teacher_in.email,
        phone=teacher_in.phone,
        address=teacher_in.address,
        blood_type=teacher_in.blood_type,
        sex=teacher_in.sex,
        birthday=teacher_in.birthday,
        img=teacher_in.img,
        user_id=user.id,
    )
    db.add(teacher)
    
    await db.commit()
    await db.refresh(user)
    
    return user


@router.post("/student/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_student(
    student_in: StudentCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_admin),
) -> Any:
    """
    Register a new student (only admins can register students)
    """
    # Check if username already exists
    result = await db.execute(select(User).filter(User.username == student_in.username))
    if result.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    
    # Create new user with student role
    user_id = student_in.id if student_in.id else str(uuid.uuid4())
    user = User(
        id=user_id,
        username=student_in.username,
        email=student_in.email,
        hashed_password=get_password_hash(student_in.password),
        role=UserRole.STUDENT,
    )
    db.add(user)
    
    # Create student record
    student = Student(
        id=user_id,
        username=student_in.username,
        name=student_in.name,
        surname=student_in.surname,
        email=student_in.email,
        phone=student_in.phone,
        address=student_in.address,
        blood_type=student_in.blood_type,
        sex=student_in.sex,
        birthday=student_in.birthday,
        img=student_in.img,
        parent_id=student_in.parent_id,
        class_id=student_in.class_id,
        grade_id=student_in.grade_id,
        user_id=user.id,
    )
    db.add(student)
    
    await db.commit()
    await db.refresh(user)
    
    return user


@router.post("/parent/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_parent(
    parent_in: ParentCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_admin),
) -> Any:
    """
    Register a new parent (only admins can register parents)
    """
    # Check if username already exists
    result = await db.execute(select(User).filter(User.username == parent_in.username))
    if result.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    
    # Create new user with parent role
    user_id = parent_in.id if parent_in.id else str(uuid.uuid4())
    user = User(
        id=user_id,
        username=parent_in.username,
        email=parent_in.email,
        hashed_password=get_password_hash(parent_in.password),
        role=UserRole.PARENT,
    )
    db.add(user)
    
    # Create parent record
    parent = Parent(
        id=user_id,
        username=parent_in.username,
        name=parent_in.name,
        surname=parent_in.surname,
        email=parent_in.email,
        phone=parent_in.phone,
        address=parent_in.address,
        user_id=user.id,
    )
    db.add(parent)
    
    await db.commit()
    await db.refresh(user)
    
    return user
