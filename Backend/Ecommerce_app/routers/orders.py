from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from Ecommerce_app.db.database import get_db
from Ecommerce_app.models.orders import orders_table, order_items_table
from Ecommerce_app.schemas.order import OrderCreate
from Ecommerce_app.auth.auth_bearer import JWTBearer
import uuid

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", dependencies=[Depends(JWTBearer())])
async def create_order(data: OrderCreate, db=Depends(get_db)):
    order_id = str(uuid.uuid4())
    stmt = insert(orders_table).values(
        id=order_id,
        user_id=str(data.user_id),
        total=data.total,
        status="pending"
    )

    await db.execute(stmt)
    
    created = await db.fetch_one(
        select(orders_table).where(orders_table.c.id == order_id)
    )
    
    return dict(created)


@router.get("/")
async def get_orders(db=Depends(get_db)):
    result = await db.fetch_all(select(orders_table))
    return [dict(row) for row in result]


@router.get("/{order_id}")
async def get_order(order_id: str, db=Depends(get_db)):
    stmt = select(orders_table).where(orders_table.c.id == order_id)
    order = await db.fetch_one(stmt)
    
    if not order:
        raise HTTPException(404, "Order not found")
    
    # Get order items
    items_stmt = select(order_items_table).where(order_items_table.c.order_id == order_id)
    items = await db.fetch_all(items_stmt)
    
    return {
        "order": dict(order),
        "items": [dict(item) for item in items]
    }