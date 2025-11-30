import uuid
from sqlalchemy import Table, Column, String, DateTime
from sqlalchemy.sql import func
from Ecommerce_app.db.database import metadata

users_table = Table(
    "users",
    metadata,
    Column("id", String(36), primary_key=True, default=lambda: str(uuid.uuid4())),
    Column("name", String(150), nullable=False),
    Column("email", String(200), unique=True, nullable=False, index=True),
    Column("hashed_password", String(255), nullable=False),  
    Column("role", String(50), server_default="user", nullable=False),
    Column("created_at", DateTime, server_default=func.now())
)