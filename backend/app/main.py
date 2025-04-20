from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Annotated
from datetime import datetime, timezone

from app.database import get_db
from app.models import *
from app.schemas import *

app = FastAPI(title="School Management API")

db_dep = Annotated[Session, Depends(get_db)]

@app.get("/")
def root():
    return {"message": "Welcome to the School Management API"}

# Grade endpoints
@app.post("/grades/", response_model=GradeResponse)
def create_grade(grade_data: GradeCreate, db: db_dep):
    db_grade = Grade(level=grade_data.level)
    db.add(db_grade)
    db.commit()
    db.refresh(db_grade)
    return db_grade

@app.get("/grades/", response_model=List[GradeResponse])
def get_grades(db: db_dep):
    grades = db.query(Grade).all()
    return grades

# Class endpoints
@app.post("/classes/", response_model=ClassResponse)
def create_class(class_data: ClassCreate, db: db_dep):
    # Check if grade exists
    grade = db.query(Grade).filter(Grade.id == class_data.grade_id).first()
    if not grade:
        raise HTTPException(status_code=404, detail="Grade not found")
    
    # Check if supervisor exists if provided
    if class_data.supervisor_id:
        teacher = db.query(Teacher).filter(Teacher.id == class_data.supervisor_id).first()
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
    
    db_class = Class(
        name=class_data.name,
        capacity=class_data.capacity,
        grade_id=class_data.grade_id,
        supervisor_id=class_data.supervisor_id
    )
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

@app.get("/classes/", response_model=List[ClassResponse])
def get_classes(db: db_dep):
    classes = db.query(Class).all()
    return classes

# Teacher endpoints
@app.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher_data: TeacherCreate, db: db_dep):
    db_teacher = Teacher(
        id=teacher_data.id,
        username=teacher_data.username,
        name=teacher_data.name,
        surname=teacher_data.surname,
        email=teacher_data.email,
        phone=teacher_data.phone,
        address=teacher_data.address,
        img=teacher_data.img,
        blood_type=teacher_data.blood_type,
        sex=teacher_data.sex,
        birthday=teacher_data.birthday
    )
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

@app.get("/teachers/", response_model=List[TeacherResponse])
def get_teachers(db: db_dep):
    teachers = db.query(Teacher).all()
    return teachers

# Parent endpoints
@app.post("/parents/", response_model=ParentResponse)
def create_parent(parent_data: ParentCreate, db: db_dep):
    db_parent = Parent(
        id=parent_data.id,
        username=parent_data.username,
        name=parent_data.name,
        surname=parent_data.surname,
        email=parent_data.email,
        phone=parent_data.phone,
        address=parent_data.address
    )
    db.add(db_parent)
    db.commit()
    db.refresh(db_parent)
    return db_parent

@app.get("/parents/", response_model=List[ParentResponse])
def get_parents(db: db_dep):
    parents = db.query(Parent).all()
    return parents

# Student endpoints
@app.post("/students/", response_model=StudentResponse)
def create_student(student_data: StudentCreate, db: db_dep):
    # Check if class exists
    class_obj = db.query(Class).filter(Class.id == student_data.class_id).first()
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")
    
    # Check if grade exists
    grade = db.query(Grade).filter(Grade.id == student_data.grade_id).first()
    if not grade:
        raise HTTPException(status_code=404, detail="Grade not found")
    
    # Check if parent exists
    parent = db.query(Parent).filter(Parent.id == student_data.parent_id).first()
    if not parent:
        raise HTTPException(status_code=404, detail="Parent not found")
    
    db_student = Student(
        id=student_data.id,
        username=student_data.username,
        name=student_data.name,
        surname=student_data.surname,
        email=student_data.email,
        phone=student_data.phone,
        address=student_data.address,
        img=student_data.img,
        blood_type=student_data.blood_type,
        sex=student_data.sex,
        birthday=student_data.birthday,
        parent_id=student_data.parent_id,
        class_id=student_data.class_id,
        grade_id=student_data.grade_id
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/students/", response_model=List[StudentResponse])
def get_students(db: db_dep):
    students = db.query(Student).all()
    return students

@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: str, db: db_dep):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
