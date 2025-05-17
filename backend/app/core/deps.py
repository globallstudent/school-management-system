from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.security import SECRET_KEY, ALGORITHM, oauth2_scheme
from app.database import SessionLocal
from app.models import User, UserRole
from app.schemas import TokenData


async def get_db() -> Generator:
    """Dependency for getting async DB session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()


async def get_current_user(
    db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> User:
    """Get the current user from the token"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    # Get the user from the database
    result = await db.execute(select(User).filter(User.username == token_data.username))
    user = result.scalars().first()
    
    if user is None:
        raise credentials_exception
    
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """Check if the current user is active"""
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def get_current_admin(current_user: User = Depends(get_current_active_user)) -> User:
    """Check if the current user is an admin"""
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    return current_user


async def get_current_teacher(current_user: User = Depends(get_current_active_user)) -> User:
    """Check if the current user is a teacher"""
    if current_user.role != UserRole.TEACHER and current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    return current_user
