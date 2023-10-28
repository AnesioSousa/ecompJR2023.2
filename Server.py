from fastapi.middleware.cors import CORSMiddleware
from hypercorn.config import Config
from hypercorn.asyncio import serve
from fastapi import FastAPI
import asyncio

from config.database.DB import init_db
from config.Config import getSettings
from routes.user.router import userRouter

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
#init_db(app)

app.include_router(userRouter)
config = Config()
config.bind = [f'127.0.0.1:{settings.APP_PORT}']

asyncio.run(serve(app, config))


