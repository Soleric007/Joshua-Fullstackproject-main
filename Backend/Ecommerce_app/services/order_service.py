from sqlalchemy import select, insert, update
from app.database import get_db
from app.models.order import orders_table
from app.models.order_item import order_items_table
from app.models.product import products_table
from app.utils.helpers import calculate_total

def create_order_service(db, user_id, items):
    """
    items: list of dicts with product_id and quantity
    """
    # Calculate total
    total = 0
    for item in items:
        stmt = select(products_table).where(products_table.c.id == item["product_id"])
        product = db.execute(stmt).first()
        if not product:
            raise Exception(f"Product {item['product_id']} not found")
        if product.stock < item["quantity"]:
            raise Exception(f"Insufficient stock for product {product.name}")
        total += product.price * item["quantity"]

    # Create order
    stmt_order = insert(orders_table).values(user_id=user_id, total=total, status="pending").returning(orders_table)
    new_order = db.execute(stmt_order).first()

    # Create order items and update stock
    for item in items:
        stmt_product = select(products_table).where(products_table.c.id == item["product_id"])
        product = db.execute(stmt_product).first()

        # Insert order item
        stmt_item = insert(order_items_table).values(
            order_id=new_order.id,
            product_id=product.id,
            quantity=item["quantity"],
            price=product.price
        )
        db.execute(stmt_item)

        # Update stock
        update_stock = (
            update(products_table)
            .where(products_table.c.id == product.id)
            .values(stock=product.stock - item["quantity"])
        )
        db.execute(update_stock)

    db.commit()
    return new_order