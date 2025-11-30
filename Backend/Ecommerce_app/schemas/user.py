from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid

class UserBase(BaseModel):
    fullname: str
    email: EmailStr
    role: str = "user"

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: uuid.UUID

    class Config:
        orm_mode = True