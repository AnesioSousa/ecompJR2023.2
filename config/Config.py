from pydantic_settings import BaseSettings
from decouple import config
from functools import lru_cache


class Settings(BaseSettings):
    APP_VERSION: str = config("APP_VERSION", default="1")
    APP_NAME: str = config("APP_NAME", default="")
    APP_DESCRIPTION: str = config("APP_DESCRIPTION", default="API")
    APP_PORT: int = config("APP_PORT", default=8080, cast=int)
    DB_URL: str = config("DB_URL")
    ORIGINS: list = ["*"]
    GENERATE_SCHEMAS: bool = config("GENERATE_SCHEMAS", default=False)
    MODELS: list = [
        "models.user.UserModel",
        "models.form.FormModel",
        "aerich.models"
    ]
    SECRET_KEY: str = config("SECRET_KEY")
    TOKEN_ALGORITHM: str = config("SECRET_KEY")
    REGISTRATION_TOKEN_LIFETIME: str = config("REGISTRATION_TOKEN_LIFETIME")

@lru_cache
def getSettings() -> Settings:
    return Settings()


