from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from models.user.UserModel import User
from models.token.TokenModel import Token
from controllers.usercontroller import UserController


#from config.Config import getSettings

from typing import Annotated
from jose import jwt

#settings = getSettings()
AuthRouter = APIRouter()
userController = UserController()

@AuthRouter.post('/signup', response_description="Checks if already has an User and if not, create an user on database")
async def createUser(request: Request) -> JSONResponse:  
    req_user = await request.json()
    print(req_user['email'])
    # email=str(req_user['email'])
    user = await userController.getOne(id=2) 
    
    if user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, # Rever esse código de resposta
            detail="User already exists"
        )
    
    
    newUser = await userController.create(user)
   
    response = jsonable_encoder(
        {
            "user": newUser,
            "detail": "User created successfully."
        }
    )
    return JSONResponse(content=response, status_code=201)

"""
@AuthRouter.post("/login", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
    
):
    
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}



@AuthRouter.get("/verify/{token}")
async def verify(token: str):
    invalid_token_error = HTTPException(status_code=400, detail="Invalid token")
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.TOKEN_ALGORITHM)
    except jwt.JWTError:
        raise HTTPException(status_code=403, detail="Token has expired")
    if payload['scope'] != 'registration':
        raise invalid_token_error
    user = await users.UserModel.get_or_none(id=payload['sub'])
    if not user or str(user.confirmation) != payload['jti']:
        raise invalid_token_error
    if user.is_active:
        raise HTTPException(status_code=403, detail="User already activated")
    user.confirmation = None
    user.is_active = True
    await user.save()
    return await users.User_Pydantic.from_tortoise_orm(user)
"""

@AuthRouter.post("/refresh")
async def refresh(token: str):
    pass