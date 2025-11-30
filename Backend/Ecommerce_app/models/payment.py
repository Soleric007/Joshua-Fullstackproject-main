import uuid
from sqlalchemy import Table, Column, String, Numeric, ForeignKey, DateTime
from sqlalchemy.sql import func
from Ecommerce_app.db.database import metadata

payments_table = Table(
    "payments",
    metadata,
    Column("id", String(36), primary_key=True, default=lambda: str(uuid.uuid4())),
    Column("order_id", String(36), ForeignKey("orders.id"), nullable=False),
    Column("amount", Numeric(10, 2), nullable=False),
    Column("method", String(50), nullable=False),
    Column("status", String(50), nullable=False, default="pending"),
    Column("transaction_id", String(150), unique=True, nullable=True),
    Column("created_at", DateTime, server_default=func.now())
)