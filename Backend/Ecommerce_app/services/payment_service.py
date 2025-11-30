from sqlalchemy import select, insert, update
from app.models.payment import payments_table
from app.models.order import orders_table

def process_payment_service(db, order_id, amount, method):
    # Get order
    stmt_order = select(orders_table).where(orders_table.c.id == order_id)
    order = db.execute(stmt_order).first()
    if not order:
        raise Exception("Order not found")

    if amount != float(order.total):
        raise Exception("Amount does not match order total")

    # Create payment
    stmt_payment = insert(payments_table).values(
        order_id=order.id,
        amount=amount,
        method=method,
        status="completed"
    ).returning(payments_table)
    payment = db.execute(stmt_payment).first()

    # Update order status
    update_order = (
        update(orders_table)
        .where(orders_table.c.id == order.id)
        .values(status="paid")
    )
    db.execute(update_order)
    db.commit()

    return payment