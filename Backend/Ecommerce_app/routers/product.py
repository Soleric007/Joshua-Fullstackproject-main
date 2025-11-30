from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, update, delete
from Ecommerce_app.db.database import get_db
from Ecommerce_app.models.product import products_table
from Ecommerce_app.schemas.product import ProductCreate, ProductResponse
import uuid

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=dict)
async def create_product(data: ProductCreate, db=Depends(get_db)):
    product_id = str(uuid.uuid4())
    stmt = insert(products_table).values(
        id=product_id,
        name=data.name,
        description=data.description,
        price=data.price,
        stock=data.stock,
        category_id=str(data.category_id)
    )

    await db.execute(stmt)
    
    created = await db.fetch_one(
        select(products_table).where(products_table.c.id == product_id)
    )
    
    return dict(created)


@router.get("/")
async def get_products(db=Depends(get_db)):
    result = await db.fetch_all(select(products_table))
    return [dict(row) for row in result]


@router.get("/{product_id}")
async def get_product(product_id: str, db=Depends(get_db)):
    stmt = select(products_table).where(products_table.c.id == product_id)
    product = await db.fetch_one(stmt)
    
    if not product:
        raise HTTPException(404, "Product not found")
    
    return dict(product)


@router.put("/{product_id}")
async def update_product(product_id: str, data: ProductCreate, db=Depends(get_db)):
    stmt = update(products_table).where(
        products_table.c.id == product_id
    ).values(
        name=data.name,
        description=data.description,
        price=data.price,
        stock=data.stock,
        category_id=str(data.category_id)
    )
    
    await db.execute(stmt)
    
    updated = await db.fetch_one(
        select(products_table).where(products_table.c.id == product_id)
    )
    
    if not updated:
        raise HTTPException(404, "Product not found")
    
    return dict(updated)


@router.delete("/{product_id}")
async def delete_product(product_id: str, db=Depends(get_db)):
    stmt = delete(products_table).where(products_table.c.id == product_id)
    await db.execute(stmt)
    return {"message": "Product deleted successfully"}