from pydantic import BaseModel, EmailStr
import uuid

class ClientBase(BaseModel):
    fullname: str
    email: EmailStr

class ClientCreate(ClientBase):
    pass

class ClientResponse(ClientBase):
    id: uuid.UUID
    balance: float

    class Config:
        orm_mode = True