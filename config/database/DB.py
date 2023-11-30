from tortoise.contrib.fastapi import register_tortoise
from config.Config import getSettings
from fastapi import FastAPI

settings = getSettings()

TORTOISE_ORM = {
    "connections": {"default": settings.DB_URL},
    "apps": {
        "models": {
            "models": settings.MODELS,
            "default_connection": "default",
        },
    },
}

def init_db(app: FastAPI) -> None:
    register_tortoise(
        app=app,
        db_url=f"postgres://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.SERVER_DATABASE_HOST}:5432/postgres",
        generate_schemas=settings.GENERATE_SCHEMAS,
        modules={"models": settings.MODELS},
        add_exception_handlers=True,
    )