from pydantic import BaseModel
import uuid

class OrderBase(BaseModel):
    user_id: uuid.UUID
    total: float
    status: str = "pending"

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: uuid.UUID

    class Config:
        orm_mode = True