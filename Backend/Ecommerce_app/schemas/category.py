from pydantic import BaseModel
import uuid

class CategoryBase(BaseModel):
    name: str
    description: str = None

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: uuid.UUID

    class Config:
        orm_mode = True