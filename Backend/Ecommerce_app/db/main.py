from Ecommerce_app.db.database import database, engine, metadata

async def startup():
    """Connect to database on startup"""
    await database.connect()
    # Create all tables
    metadata.create_all(engine)
    print("✅ Database connected and tables created!")

async def shutdown():
    """Disconnect from database on shutdown"""
    await database.disconnect()
    print("✅ Database disconnected!")