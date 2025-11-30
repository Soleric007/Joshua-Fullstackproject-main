from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from Ecommerce_app.db.database import get_db
from Ecommerce_app.models.users import users_table
from Ecommerce_app.schemas.user import UserCreate, UserResponse
from Ecommerce_app.auth.auth import create_access_token
from Ecommerce_app.auth.hash import hash_password, verify_password
import uuid

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=dict)
async def register(data: UserCreate, db=Depends(get_db)):
    # Check if user exists
    query = select(users_table).where(users_table.c.email == data.email)
    result = await db.fetch_one(query)

    if result:
        raise HTTPException(status_code=400, detail="Email already exists")

    # Create new user
    user_id = str(uuid.uuid4())
    new_user = {
        "id": user_id,
        "name": data.fullname,
        "email": data.email,
        "hashed_password": hash_password(data.password),
        "role": data.role
    }

    stmt = insert(users_table).values(new_user)
    await db.execute(stmt)

    # Get created user
    created_user = await db.fetch_one(
        select(users_table).where(users_table.c.id == user_id)
    )

    # Create token
    token = create_access_token({"id": str(created_user["id"]), "role": created_user["role"]})

    return {
        "token": token,
        "user": {
            "id": str(created_user["id"]),
            "name": created_user["name"],
            "email": created_user["email"],
            "role": created_user["role"]
        }
    }
    

@router.post("/login")
async def login(data: UserCreate, db=Depends(get_db)):
    query = select(users_table).where(users_table.c.email == data.email)
    user = await db.fetch_one(query)

    if not user or not verify_password(data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"id": str(user["id"]), "role": user["role"]})

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": str(user["id"]),
            "name": user["name"],
            "email": user["email"],
            "role": user["role"]
        }
    }