import jwt
from datetime import datetime, timedelta
from Ecommerce_app.db.config import config

def create_access_token(data: dict, expires_minutes: int = None):
    """
    Create a JWT token with expiration.
    data: dict (e.g., {"id": user_id, "role": user_role})
    """
    to_encode = data.copy()
    if expires_minutes is None:
        expires_minutes = config.ACCESS_TOKEN_EXPIRE_MINUTES
    
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return token


def decode_access_token(token: str):
    """
    Decode a JWT token and return payload.
    Returns None if token is invalid or expired.
    """
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None