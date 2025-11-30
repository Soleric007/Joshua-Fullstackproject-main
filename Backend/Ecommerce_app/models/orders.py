import uuid
from sqlalchemy import Table, Column, String, DateTime, ForeignKey, Numeric, Integer
from sqlalchemy.sql import func
from Ecommerce_app.db.database import metadata

orders_table = Table(
    "orders",
    metadata,
    Column("id", String(36), primary_key=True, default=lambda: str(uuid.uuid4())),
    Column("user_id", String(36), ForeignKey("users.id"), nullable=False),
    Column("total", Numeric(10, 2), nullable=False),
    Column("order_date", DateTime, server_default=func.now(), nullable=False),
    Column("status", String(50), nullable=False, server_default="pending")
)

order_items_table = Table(
    "order_items",
    metadata,
    Column("id", String(36), primary_key=True, default=lambda: str(uuid.uuid4())),
    Column("order_id", String(36), ForeignKey("orders.id"), nullable=False),
    Column("product_id", String(36), ForeignKey("products.id"), nullable=False),
    Column("quantity", Integer, nullable=False),
    Column("price", Numeric(10, 2), nullable=False)
)