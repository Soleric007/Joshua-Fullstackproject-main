from pydantic import BaseModel
import uuid

class PaymentBase(BaseModel):
    order_id: uuid.UUID
    amount: float
    method: str
    status: str = "completed"

class PaymentCreate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    id: uuid.UUID

    class Config:
        orm_mode = True