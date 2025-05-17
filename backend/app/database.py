# database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# Use environment variables for database connection
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "2021")
POSTGRES_SERVER = os.getenv("POSTGRES_SERVER", "localhost")
POSTGRES_DB = os.getenv("POSTGRES_DB", "school_management_db")

DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()
