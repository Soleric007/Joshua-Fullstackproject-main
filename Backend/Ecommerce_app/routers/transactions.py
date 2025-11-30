from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, update
from Ecommerce_app.db.database import get_db
from Ecommerce_app.models.client import clients_table
from Ecommerce_app.auth.auth_bearer import JWTBearer

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/deposit", dependencies=[Depends(JWTBearer())])
async def deposit(client_id: str, amount: float, db=Depends(get_db)):
    stmt = select(clients_table).where(clients_table.c.id == client_id)
    client = await db.fetch_one(stmt)

    if not client:
        raise HTTPException(404, "Client not found")

    new_balance = float(client["balance"]) + amount

    update_stmt = update(clients_table).where(
        clients_table.c.id == client_id
    ).values(balance=new_balance)

    await db.execute(update_stmt)

    return {"message": "Deposit successful", "new_balance": new_balance}