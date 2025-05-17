from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    """Token schema for JWT authentication"""
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Token data schema for JWT authentication"""
    username: Optional[str] = None
