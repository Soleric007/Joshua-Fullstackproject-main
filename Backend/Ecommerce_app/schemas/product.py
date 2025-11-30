from pydantic import BaseModel
import uuid

class ProductBase(BaseModel):
    name: str
    description: str = None
    price: float
    stock: int
    category_id: uuid.UUID

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: uuid.UUID

    class Config:
        orm_mode = True