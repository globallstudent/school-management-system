-- Create enum types
CREATE TYPE userrole AS ENUM ('ADMIN', 'TEACHER', 'STUDENT', 'PARENT');
CREATE TYPE usersex AS ENUM ('MALE', 'FEMALE');
CREATE TYPE dayofweek AS ENUM ('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY');

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR PRIMARY KEY,
    username VARCHAR NOT NULL UNIQUE,
    email VARCHAR UNIQUE,
    hashed_password VARCHAR NOT NULL,
    role userrole NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL
);

-- Create grades table
CREATE TABLE IF NOT EXISTS grades (
    id SERIAL PRIMARY KEY,
    level INTEGER NOT NULL UNIQUE
);

-- Create admins table
CREATE TABLE IF NOT EXISTS admins (
    id VARCHAR PRIMARY KEY,
    username VARCHAR NOT NULL UNIQUE,
    user_id VARCHAR NOT NULL REFERENCES users(id)
);

-- Create teachers table
CREATE TABLE IF NOT EXISTS teachers (
    id VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL,
    surname VARCHAR NOT NULL,
    address VARCHAR NOT NULL,
    phone VARCHAR UNIQUE,
    email VARCHAR UNIQUE,
    img VARCHAR,
    blood_type VARCHAR,
    sex usersex NOT NULL,
    created_at TIMESTAMP NOT NULL,
    birthday TIMESTAMP NOT NULL,
    user_id VARCHAR NOT NULL REFERENCES users(id)
);

-- Create parents table
CREATE TABLE IF NOT EXISTS parents (
    id VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL,
    surname VARCHAR NOT NULL,
    address VARCHAR NOT NULL,
    phone VARCHAR NOT NULL UNIQUE,
    email VARCHAR UNIQUE,
    created_at TIMESTAMP NOT NULL,
    user_id VARCHAR NOT NULL REFERENCES users(id)
);

-- Create classes table
CREATE TABLE IF NOT EXISTS classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL UNIQUE,
    capacity INTEGER NOT NULL,
    supervisor_id VARCHAR REFERENCES teachers(id),
    grade_id INTEGER NOT NULL REFERENCES grades(id)
);

-- Create students table
CREATE TABLE IF NOT EXISTS students (
    id VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL,
    surname VARCHAR NOT NULL,
    address VARCHAR NOT NULL,
    phone VARCHAR UNIQUE,
    email VARCHAR UNIQUE,
    img VARCHAR,
    blood_type VARCHAR NOT NULL,
    sex usersex NOT NULL,
    created_at TIMESTAMP NOT NULL,
    birthday TIMESTAMP NOT NULL,
    user_id VARCHAR NOT NULL REFERENCES users(id),
    parent_id VARCHAR NOT NULL REFERENCES parents(id),
    class_id INTEGER NOT NULL REFERENCES classes(id),
    grade_id INTEGER NOT NULL REFERENCES grades(id)
);

-- Create subjects table
CREATE TABLE IF NOT EXISTS subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL UNIQUE
);

-- Create teacher_subject association table
CREATE TABLE IF NOT EXISTS teacher_subject (
    teacher_id VARCHAR NOT NULL REFERENCES teachers(id),
    subject_id INTEGER NOT NULL REFERENCES subjects(id),
    PRIMARY KEY (teacher_id, subject_id)
);

-- Create lessons table
CREATE TABLE IF NOT EXISTS lessons (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    day dayofweek NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    subject_id INTEGER NOT NULL REFERENCES subjects(id),
    class_id INTEGER NOT NULL REFERENCES classes(id),
    teacher_id VARCHAR NOT NULL REFERENCES teachers(id)
);

-- Create exams table
CREATE TABLE IF NOT EXISTS exams (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    lesson_id INTEGER NOT NULL REFERENCES lessons(id)
);

-- Create assignments table
CREATE TABLE IF NOT EXISTS assignments (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    description VARCHAR,
    start_date TIMESTAMP NOT NULL,
    due_date TIMESTAMP NOT NULL,
    lesson_id INTEGER NOT NULL REFERENCES lessons(id)
);

-- Create results table
CREATE TABLE IF NOT EXISTS results (
    id SERIAL PRIMARY KEY,
    score INTEGER NOT NULL,
    exam_id INTEGER REFERENCES exams(id),
    assignment_id INTEGER REFERENCES assignments(id),
    student_id VARCHAR NOT NULL REFERENCES students(id)
);

-- Create attendances table
CREATE TABLE IF NOT EXISTS attendances (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP NOT NULL,
    present BOOLEAN NOT NULL,
    student_id VARCHAR NOT NULL REFERENCES students(id),
    lesson_id INTEGER NOT NULL REFERENCES lessons(id)
);

-- Create events table
CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    class_id INTEGER REFERENCES classes(id)
);

-- Create announcements table
CREATE TABLE IF NOT EXISTS announcements (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    date TIMESTAMP NOT NULL,
    class_id INTEGER REFERENCES classes(id)
);
