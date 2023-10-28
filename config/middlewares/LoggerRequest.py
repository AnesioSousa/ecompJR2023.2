from fastapi import FastAPI, Request
from hypercorn.logging import Logger
import logging

class LoggerRequestMiddleware:
    def __init__(self, app: FastAPI, logger: Logger) -> None:
        self.app = app
        self.logger = logger

    async def __call__(self, request: Request) -> None:
        self.logger.debug(request.url)