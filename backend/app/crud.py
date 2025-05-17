# crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from typing import List, Optional, Any, Dict, Type, TypeVar, Generic

from app.core.security import get_password_hash, verify_password
from app.models import (
    User,
    Admin,
    Student,
    Teacher,
    Parent,
    Class,
    Grade,
    Subject,
    Lesson,
    Exam,
    Assignment,
    Result,
    Attendance,
    Event,
    Announcement,
)
from app.schemas import (
    UserCreate,
    AdminCreate,
    StudentCreate,
    TeacherCreate,
    ParentCreate,
    ClassCreate,
    GradeCreate,
    SubjectCreate,
    LessonCreate,
    ExamCreate,
    AssignmentCreate,
    ResultCreate,
    AttendanceCreate,
    EventCreate,
    AnnouncementCreate,
)

# Generic type for the model
ModelType = TypeVar("ModelType")
# Generic type for the schema used to create data
CreateSchemaType = TypeVar("CreateSchemaType")


class CRUDBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, db: AsyncSession, id: Any) -> Optional[ModelType]:
        result = await db.execute(select(self.model).filter(self.model.id == id))
        return result.scalars().first()

    async def get_multi(
        self, db: AsyncSession, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        result = await db.execute(select(self.model).offset(skip).limit(limit))
        return result.scalars().all()

    async def create(self, db: AsyncSession, *, obj_in: CreateSchemaType) -> ModelType:
        db_obj = self.model(**obj_in.dict())
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(
        self, db: AsyncSession, *, db_obj: ModelType, obj_in: Dict[str, Any]
    ) -> ModelType:
        await db.execute(
            update(self.model).where(self.model.id == db_obj.id).values(**obj_in)
        )
        await db.commit()
        return await self.get(db, id=db_obj.id)

    async def remove(self, db: AsyncSession, *, id: Any) -> ModelType:
        obj = await self.get(db, id)
        if obj:
            await db.execute(delete(self.model).where(self.model.id == id))
            await db.commit()
        return obj


# Create specific CRUD classes for different models
class CRUDStudent(CRUDBase[Student, StudentCreate]):
    async def get_by_username(
        self, db: AsyncSession, *, username: str
    ) -> Optional[Student]:
        result = await db.execute(select(Student).filter(Student.username == username))
        return result.scalars().first()

    async def get_by_email(self, db: AsyncSession, *, email: str) -> Optional[Student]:
        result = await db.execute(select(Student).filter(Student.email == email))
        return result.scalars().first()

    async def get_by_class(self, db: AsyncSession, *, class_id: int) -> List[Student]:
        result = await db.execute(select(Student).filter(Student.class_id == class_id))
        return result.scalars().all()

    async def get_by_grade(self, db: AsyncSession, *, grade_id: int) -> List[Student]:
        result = await db.execute(select(Student).filter(Student.grade_id == grade_id))
        return result.scalars().all()

    async def get_by_parent(self, db: AsyncSession, *, parent_id: str) -> List[Student]:
        result = await db.execute(
            select(Student).filter(Student.parent_id == parent_id)
        )
        return result.scalars().all()


class CRUDTeacher(CRUDBase[Teacher, TeacherCreate]):
    async def get_by_username(
        self, db: AsyncSession, *, username: str
    ) -> Optional[Teacher]:
        result = await db.execute(select(Teacher).filter(Teacher.username == username))
        return result.scalars().first()

    async def get_by_email(self, db: AsyncSession, *, email: str) -> Optional[Teacher]:
        result = await db.execute(select(Teacher).filter(Teacher.email == email))
        return result.scalars().first()


class CRUDClass(CRUDBase[Class, ClassCreate]):
    async def get_by_name(self, db: AsyncSession, *, name: str) -> Optional[Class]:
        result = await db.execute(select(Class).filter(Class.name == name))
        return result.scalars().first()

    async def get_by_grade(self, db: AsyncSession, *, grade_id: int) -> List[Class]:
        result = await db.execute(select(Class).filter(Class.grade_id == grade_id))
        return result.scalars().all()

    async def get_by_supervisor(
        self, db: AsyncSession, *, supervisor_id: str
    ) -> List[Class]:
        result = await db.execute(
            select(Class).filter(Class.supervisor_id == supervisor_id)
        )
        return result.scalars().all()


class CRUDUser(CRUDBase[User, UserCreate]):
    async def get_by_username(self, db: AsyncSession, *, username: str) -> Optional[User]:
        result = await db.execute(select(User).filter(User.username == username))
        return result.scalars().first()

    async def get_by_email(self, db: AsyncSession, *, email: str) -> Optional[User]:
        result = await db.execute(select(User).filter(User.email == email))
        return result.scalars().first()

    async def create(self, db: AsyncSession, *, obj_in: UserCreate) -> User:
        db_obj = User(
            username=obj_in.username,
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            role=obj_in.role,
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update_password(self, db: AsyncSession, *, user: User, password: str) -> User:
        user.hashed_password = get_password_hash(password)
        await db.commit()
        await db.refresh(user)
        return user

    async def authenticate(self, db: AsyncSession, *, username: str, password: str) -> Optional[User]:
        user = await self.get_by_username(db, username=username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user


class CRUDParent(CRUDBase[Parent, ParentCreate]):
    async def get_by_username(self, db: AsyncSession, *, username: str) -> Optional[Parent]:
        result = await db.execute(select(Parent).filter(Parent.username == username))
        return result.scalars().first()

    async def get_by_email(self, db: AsyncSession, *, email: str) -> Optional[Parent]:
        result = await db.execute(select(Parent).filter(Parent.email == email))
        return result.scalars().first()


# Initialize CRUD instances
user = CRUDUser(User)
admin = CRUDBase[Admin, AdminCreate](Admin)
student = CRUDStudent(Student)
teacher = CRUDTeacher(Teacher)
parent = CRUDParent(Parent)
class_ = CRUDClass(Class)
grade = CRUDBase[Grade, GradeCreate](Grade)
subject = CRUDBase[Subject, SubjectCreate](Subject)
lesson = CRUDBase[Lesson, LessonCreate](Lesson)
exam = CRUDBase[Exam, ExamCreate](Exam)
assignment = CRUDBase[Assignment, AssignmentCreate](Assignment)
result = CRUDBase[Result, ResultCreate](Result)
attendance = CRUDBase[Attendance, AttendanceCreate](Attendance)
event = CRUDBase[Event, EventCreate](Event)
announcement = CRUDBase[Announcement, AnnouncementCreate](Announcement)
