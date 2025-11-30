import databases
import sqlalchemy
from Ecommerce_app.db.config import config

metadata = sqlalchemy.MetaData()

# Create engine
engine = sqlalchemy.create_engine(
    config.DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# Create database instance
database = databases.Database(
    config.DATABASE_URL, 
    force_rollback=config.DB_FORCE_ROLLBACK
)

# Dependency for getting database session
def get_db():
    """
    Database dependency for FastAPI routes.
    Usage: db = Depends(get_db)
    """
    return database