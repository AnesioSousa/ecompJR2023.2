from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from controllers.UserController import UserController
from dtos.user.userDTO import UserDTO


userRouter = APIRouter(prefix="/api/v1")
userController = UserController()

@userRouter.api_route('/create-user', response_description="Create an user on database", methods=["POST"])
async def createUser(request: Request) -> JSONResponse:  
    user = await request.json()
    newUser = await userController.create(user)
   
    response = jsonable_encoder(
        {
            "user": newUser,
            "detail": "User created successfully."
        }
    )
    return JSONResponse(content=response, status_code=201)

@userRouter.api_route('/update-user', response_description="Update an user on database", methods=["PUT"])
async def updateUser(request: Request) -> JSONResponse:
    user = await request.json()
    updatedUser = await userController.update(user)

    response = jsonable_encoder(
        {
            "user": updatedUser,
            "detail": "User updated successfully."
        }
    )
    return JSONResponse(content=response, status_code=200)

@userRouter.api_route('/read-user', response_description="Read all the users from database", methods=["GET"])
async def readUsers() -> JSONResponse:
    users = await userController.getAll()

    response = jsonable_encoder(
        {
            "user": users,
            "detail": "Users read successfully."
        }
    )
    return JSONResponse(content=response, status_code=200)

@userRouter.api_route('/read-user/{user_id}', response_description="Read an user from database", methods=["GET"])
async def readUser(user_id: int) -> JSONResponse:
    user = await userController.getOne(user_id)

    response = jsonable_encoder(
        {
            "user": user,
            "detail": "User read successfully."
        }
    )
    return JSONResponse(content=response, status_code=200)

@userRouter.api_route('/delete-user/{user_id}', response_description="Delete an user from database", methods=["DELETE"])
async def deleteUser(user_id: int) -> JSONResponse:
    await userController.delete(user_id)
    return JSONResponse(content='', status_code=204)