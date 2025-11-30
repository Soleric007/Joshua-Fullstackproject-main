import uuid
from sqlalchemy import Table, Column, String, Text
from Ecommerce_app.db.database import metadata

categories_table = Table(
    "categories",
    metadata,
    Column("id", String(36), primary_key=True, default=lambda: str(uuid.uuid4())),
    Column("name", String(100), nullable=False, unique=True),
    Column("description", Text, nullable=True)
)