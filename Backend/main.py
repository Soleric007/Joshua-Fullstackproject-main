from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Ecommerce_app.db.main import startup, shutdown
from Ecommerce_app.routers import auth, category, product, orders, payment, client, transactions

# Create FastAPI app
app = FastAPI(
    title="E-commerce API",
    description="Full-featured e-commerce backend API",
    version="1.0.0"
)

# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth.router)
app.include_router(category.router)
app.include_router(product.router)
app.include_router(orders.router)
app.include_router(payment.router)
app.include_router(client.router)
app.include_router(transactions.router)

# Startup and shutdown events
@app.on_event("startup")
async def on_startup():
    await startup()

@app.on_event("shutdown")
async def on_shutdown():
    await shutdown()

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "E-commerce API is running!",
        "version": "1.0.0",
        "docs": "/docs"
    }

# Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy"}