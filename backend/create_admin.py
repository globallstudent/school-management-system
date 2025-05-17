#!/usr/bin/env python
"""
Script to create the initial admin user for the School Management System.
Run this script once to bootstrap the system with an admin user.
"""
import asyncio
import uuid
import datetime
from getpass import getpass

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import SessionLocal
from app.models import User, Admin, UserRole
from app.core.security import get_password_hash


async def create_admin():
    """Create an admin user if no admin exists."""
    db = SessionLocal()
    try:
        # Check if any admin user exists
        result = await db.execute(select(User).filter(User.role == UserRole.ADMIN))
        existing_admin = result.scalars().first()
        
        if existing_admin:
            print(f"Admin user already exists: {existing_admin.username}")
            return
        
        # Use predefined values for admin user
        print("Creating initial admin user...")
        username = "admin"
        password = "admin123"
        
        # Check if username already exists
        result = await db.execute(select(User).filter(User.username == username))
        if result.scalars().first():
            print(f"Error: Username '{username}' already exists")
            return
        
        print(f"Creating admin user with username: {username}")
        print("Note: Default password is 'admin123'. Please change it after first login.")

        
        # Create user with admin role
        user_id = str(uuid.uuid4())
        user = User(
            id=user_id,
            username=username,
            hashed_password=get_password_hash(password),
            role=UserRole.ADMIN,
            is_active=True,
            created_at=datetime.datetime.now()
        )
        db.add(user)
        
        # Create admin record
        admin = Admin(
            id=user_id,
            username=username,
            user_id=user.id
        )
        db.add(admin)
        
        await db.commit()
        print(f"Admin user '{username}' created successfully!")
        
    except Exception as e:
        print(f"Error creating admin user: {e}")
    finally:
        await db.close()


if __name__ == "__main__":
    asyncio.run(create_admin())
