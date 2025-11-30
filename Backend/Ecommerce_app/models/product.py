import uuid
from sqlalchemy import Table, Column, String, Text, Numeric, ForeignKey, DateTime, Integer
from sqlalchemy.sql import func
from Ecommerce_app.db.database import metadata

products_table = Table(
    "products",
    metadata,
    Column("id", String(36), primary_key=True, default=lambda: str(uuid.uuid4())),
    Column("name", String(150), nullable=False),
    Column("description", Text, nullable=True),
    Column("price", Numeric(10, 2), nullable=False),
    Column("stock", Integer, nullable=False, default=0),
    Column("category_id", String(36), ForeignKey("categories.id"), nullable=False),
    Column("created_at", DateTime, server_default=func.now())
)