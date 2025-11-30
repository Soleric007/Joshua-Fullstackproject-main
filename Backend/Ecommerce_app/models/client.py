import uuid
from sqlalchemy import Table, Column, String, Numeric
from Ecommerce_app.db.database import metadata

clients_table = Table(
    "clients",
    metadata,
    Column("id", String(36), primary_key=True, default=lambda: str(uuid.uuid4())),
    Column("fullname", String(150), nullable=False),
    Column("email", String(200), nullable=False, unique=True),
    Column("balance", Numeric(12, 2), nullable=False, default=0.00)
)