from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from Ecommerce_app.db.database import get_db
from Ecommerce_app.models.payment import payments_table
from Ecommerce_app.schemas.payment import PaymentCreate
from Ecommerce_app.auth.auth_bearer import JWTBearer
import uuid

router = APIRouter(prefix="/payments", tags=["Payments"])


@router.post("/", dependencies=[Depends(JWTBearer())])
async def create_payment(data: PaymentCreate, db=Depends(get_db)):
    payment_id = str(uuid.uuid4())
    stmt = insert(payments_table).values(
        id=payment_id,
        order_id=str(data.order_id),
        amount=data.amount,
        method=data.method,
        status="completed"
    )

    await db.execute(stmt)
    
    created = await db.fetch_one(
        select(payments_table).where(payments_table.c.id == payment_id)
    )
    
    return dict(created)


@router.get("/")
async def get_payments(db=Depends(get_db)):
    result = await db.fetch_all(select(payments_table))
    return [dict(row) for row in result]