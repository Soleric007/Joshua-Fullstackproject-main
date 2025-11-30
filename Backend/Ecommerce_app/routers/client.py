from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from Ecommerce_app.db.database import get_db
from Ecommerce_app.models.users import users_table

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def get_users(db=Depends(get_db)):
    result = await db.fetch_all(select(users_table))
    return [dict(row) for row in result]


@router.get("/{user_id}")
async def get_user(user_id: str, db=Depends(get_db)):
    stmt = select(users_table).where(users_table.c.id == user_id)
    user = await db.fetch_one(stmt)

    if not user:
        raise HTTPException(404, "User not found")

    return dict(user)