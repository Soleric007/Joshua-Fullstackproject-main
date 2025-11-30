from pydantic import BaseModel
import uuid

class OrderItemBase(BaseModel):
    order_id: uuid.UUID
    product_id: uuid.UUID
    quantity: int
    price: float

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemResponse(OrderItemBase):
    id: uuid.UUID

    class Config:
        orm_mode = True