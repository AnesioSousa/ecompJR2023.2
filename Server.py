from fastapi.middleware.cors import CORSMiddleware
from hypercorn.config import Config
from hypercorn.asyncio import serve
from fastapi import FastAPI
import asyncio
import logging

from config.database.DB import init_db
from config.Config import getSettings
from routes.form.router import formRouter

settings = getSettings()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
)
app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=settings.ORIGINS
)
init_db(app)

app.include_router(formRouter)

config = Config()

config.bind = [f'0.0.0.0:{settings.APP_PORT}']

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("hypercorn")
logger.setLevel(logging.INFO)
config.accesslog = logger

config.use_reloader = True

asyncio.run(serve(app, config))


