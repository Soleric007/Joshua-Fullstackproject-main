from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class BaseConfig(BaseSettings):
    DATABASE_URL: Optional[str] = "sqlite:///./ecommerce.db"
    DB_FORCE_ROLLBACK: bool = False
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

class GlobalConfig(BaseConfig):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

config = GlobalConfig()