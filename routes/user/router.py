from fastapi import APIRouter, Request


userRouter = APIRouter()

@userRouter.get('/health', response_description="Returns the health of the server")
async def getHealth(request: Request):
    return request.headers