import time
from fastapi import HTTPException

# Example in-memory rate limit dictionary
# For production, use Redis or another persistent store
RATE_LIMIT_STORE = {}

def rate_limit(key: str, limit: int = 5, period_seconds: int = 60):
    """Simple rate limiting"""
    now = int(time.time())
    if key not in RATE_LIMIT_STORE:
        RATE_LIMIT_STORE[key] = []
    # Remove expired timestamps
    RATE_LIMIT_STORE[key] = [t for t in RATE_LIMIT_STORE[key] if t > now - period_seconds]

    if len(RATE_LIMIT_STORE[key]) >= limit:
        raise HTTPException(status_code=429, detail="Too many requests")

    RATE_LIMIT_STORE[key].append(now)