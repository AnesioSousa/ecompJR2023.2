from controllers.FormController import FormController
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

formRouter = APIRouter(prefix="/api/v1")
formController = FormController()

@formRouter.api_route('/create-form', response_description="Create an form on database", methods=["POST"])
async def createUser(request: Request) -> JSONResponse:
    form = await request.json()
    newForm = await formController.create(form)
   
    response = jsonable_encoder(
        {
            "form": newForm,
            "detail": "Form created successfully."
        }
    )
    return JSONResponse(content=response, status_code=201)

