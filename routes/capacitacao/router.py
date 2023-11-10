from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.user.UserModel import User


capacitacaoRouter = APIRouter()

@capacitacaoRouter.post('/api/v1/criar-usuario', response_description="Create user and returns the resource")
async def createUser(request: Request, user: User) -> JSONResponse:
    #Usuário pode ser pego direto ou através do body da Request do modo na linha abaixo
    #user = await request.json()
    
    response = jsonable_encoder(
        {
            "user": user,
            "message": "User created successfully."
        }
    )
    #headers também poderiam ser setados, caso necessário, senão o padrão é setado pelo Framework.
    return JSONResponse(content=response, status_code=200)
