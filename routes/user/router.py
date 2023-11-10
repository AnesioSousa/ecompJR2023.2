from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from controllers.UserController import UserController
from dtos.user.userDTO import UserDTO


userRouter = APIRouter(prefix="/api/v1")
userController = UserController()

@userRouter.api_route('/create-user', response_description="Create an user", methods=["POST"])
async def createUser(request: Request) -> JSONResponse:  
    user = await request.json()
    newUser = await userController.create(user)
   
    response = jsonable_encoder(
        {
            "user": newUser,
            "message": "User created successfully."
        }
    )
    return JSONResponse(content=response, status_code=200)

@userRouter.api_route('/update-user', response_description="Update an user", methods=["PUT"])
async def updateUser(request: Request) -> JSONResponse:
    user = await request.json()
    updatedUser = await userController.update(user)
    print(updatedUser)
    response = jsonable_encoder(
        {
            "user": updatedUser,
            "message": "User created successfully."
        }
    )#TODO: verificar se é possível fazer isso aqui utilizando o DTO, pois envolve o getOne e o Update.
    return JSONResponse(content=response, status_code=200)