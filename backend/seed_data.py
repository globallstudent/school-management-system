from app.database import SessionLocal
from app.models import *
from app.schemas import (
    GradeCreate,
    ClassCreate,
    TeacherCreate,
    StudentCreate,
    ParentCreate,
)
from app.crud import grade, class_, teacher, student, parent
import asyncio
from datetime import datetime, timezone
from enum import Enum


class UserSex(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


async def seed_database():
    async with SessionLocal() as db:
        # Create a grade
        grade_data = GradeCreate(level=1)
        grade_obj = await grade.create(db, obj_in=grade_data)

        # Create a teacher
        teacher_data = TeacherCreate(
            id="teacher1",
            username="teacher1",
            name="John",
            surname="Doe",
            email="teacher1@example.com",
            phone="1234567890",
            address="123 Teacher St",
            blood_type="A+",
            sex=UserSex.MALE,
            birthday=datetime(1980, 1, 1, tzinfo=timezone.utc),
        )
        teacher_obj = await teacher.create(db, obj_in=teacher_data)

        # Create a class
        class_data = ClassCreate(
            name="Class 1A",
            capacity=30,
            grade_id=grade_obj.id,
            supervisor_id=teacher_obj.id,
        )
        class_obj = await class_.create(db, obj_in=class_data)

        # Create a parent
        parent_data = ParentCreate(
            id="parent1",
            username="parent1",
            name="Jane",
            surname="Smith",
            email="parent1@example.com",
            phone="0987654321",
            address="456 Parent Ave",
        )
        parent_obj = await parent.create(db, obj_in=parent_data)

        # Create a student
        student_data = StudentCreate(
            id="student1",
            username="student1",
            name="Alice",
            surname="Johnson",
            email="student1@example.com",
            phone="1112223333",
            address="789 Student Blvd",
            blood_type="O+",
            sex=UserSex.FEMALE,
            birthday=datetime(2010, 1, 1, tzinfo=timezone.utc),
            parent_id=parent_obj.id,
            class_id=class_obj.id,
            grade_id=grade_obj.id,
        )
        await student.create(db, obj_in=student_data)

        await db.commit()


if __name__ == "__main__":
    asyncio.run(seed_database())
