from sqlalchemy import select
from app.models.product import products_table

def get_product_by_id(db, product_id):
    stmt = select(products_table).where(products_table.c.id == product_id)
    product = db.execute(stmt).first()
    if not product:
        raise Exception("Product not found")
    return product

def check_stock(db, product_id, quantity):
    product = get_product_by_id(db, product_id)
    if product.stock < quantity:
        raise Exception(f"Not enough stock for {product.name}")
    return True