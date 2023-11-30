from pydantic_settings import BaseSettings
from decouple import config
from functools import lru_cache
"""
        
        "services.models.user.UserModel",
        "services.models.token.TokenModel"
"""

class Settings(BaseSettings):
    APP_VERSION: str = config("APP_VERSION", default="1")
    APP_NAME: str = config("APP_NAME", default="")
    APP_DESCRIPTION: str = config("APP_DESCRIPTION", default="API")
    APP_PORT: int = config("APP_PORT", default=8080, cast=int)
    DB_URL: str = config("DB_URL")
    ORIGINS: list = ["*"]
    GENERATE_SCHEMAS: bool = config("GENERATE_SCHEMAS", default=False)
    MODELS: list = [
        "models.form.FormModel",
        "aerich.models"
    ]
    ACCESS_TOKEN_SECRET: str = config("ACCESS_TOKEN_SECRET")
    REFRESH_TOKEN_SECRET: str = config("REFRESH_TOKEN_SECRET")
    REFRESH_TOKEN_EXPIRATION: str = config("REFRESH_TOKEN_EXPIRATION", default=60)
    SERVER_AUTH_PORT: int = config("SERVER_AUTH_PORT") 
    SERVER_DATABASE_HOST: str = config("SERVER_DATABASE_HOST")
    POSTGRES_USER: str = config("POSTGRES_USER")
    POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD")

@lru_cache
def getSettings() -> Settings:
    """Singleton instance"""
    return Settings()


