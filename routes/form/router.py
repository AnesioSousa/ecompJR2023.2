from controllers.FormController import FormController
from config.Config import getSettings
from fastapi import APIRouter, Request, HTTPException, Depends, Header
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2AuthorizationCodeBearer
from jose import JWTError, jwt

formRouter = APIRouter(prefix="/api/v1")
formController = FormController()
settings = getSettings()

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    tokenUrl="login",
    authorizationUrl="signup",  # Replace with the actual authorization URL
)

async def authenticate_token(authorization: str = Header(..., description="Authorization header")):
    token_prefix = "Bearer "
    token = authorization.replace(token_prefix, "")
    
    if not token:
        raise HTTPException(status_code=400, detail="Error: Login required to continue!")

    try:
        payload = jwt.decode(token, settings.ACCESS_TOKEN_SECRET, algorithms=["HS256"])
    except JWTError:
        raise HTTPException(status_code=401, detail="Error: Login required to continue!")

    return payload

@formRouter.api_route('/create-form', response_description="Create an form on database", methods=["POST"])
async def createForm(request: Request) -> JSONResponse:
    form = await request.json()
    newForm = await formController.create(form)
   
    response = jsonable_encoder(
        {
            "form": newForm,
            "detail": "Form created successfully."
        }
    )
    return JSONResponse(content=response, status_code=201)

@formRouter.api_route('/read-form', response_description="Read all the forms from database",methods=["GET"])
async def readForms(token: dict = Depends(authenticate_token)) -> JSONResponse:
    forms = await formController.getAll()

    response = jsonable_encoder(
        {
            "form": forms,
            "detail": "Forms read successfully."
        }
    )
    return JSONResponse(content=response, status_code=200)

@formRouter.api_route('/read-form/{form_id}', response_description="Read a form from database", methods=["GET"])
async def readForm(form_id: int, token: dict = Depends(authenticate_token)) -> JSONResponse:
    form = await formController.getOne(form_id)

    response = jsonable_encoder(
        {
            "form": form,
            "detail": "Form read successfully."
        }
    )
    return JSONResponse(content=response, status_code=200)