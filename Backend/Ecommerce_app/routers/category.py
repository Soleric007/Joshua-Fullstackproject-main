from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from Ecommerce_app.db.database import get_db
from Ecommerce_app.models.category import categories_table
from Ecommerce_app.schemas.category import CategoryCreate, CategoryResponse
import uuid

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/", response_model=dict)
async def create_category(data: CategoryCreate, db=Depends(get_db)):
    category_id = str(uuid.uuid4())
    stmt = insert(categories_table).values(
        id=category_id,
        name=data.name,
        description=data.description
    )

    await db.execute(stmt)
    
    created = await db.fetch_one(
        select(categories_table).where(categories_table.c.id == category_id)
    )
    
    return dict(created)


@router.get("/")
async def get_categories(db=Depends(get_db)):
    result = await db.fetch_all(select(categories_table))
    return [dict(row) for row in result]


@router.get("/{category_id}")
async def get_category(category_id: str, db=Depends(get_db)):
    stmt = select(categories_table).where(categories_table.c.id == category_id)
    category = await db.fetch_one(stmt)
    
    if not category:
        raise HTTPException(404, "Category not found")
    
    return dict(category)