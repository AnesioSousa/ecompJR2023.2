from controllers.FormController import FormController
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

formRouter = APIRouter(prefix="/api/v1")
formController = FormController()

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

@formRouter.api_route('/read-form', response_description="Read all the forms from database", methods=["GET"])
async def readForms() -> JSONResponse:
    forms = await formController.getAll()

    response = jsonable_encoder(
        {
            "form": forms,
            "detail": "Forms read successfully."
        }
    )
    return JSONResponse(content=response, status_code=200)

@formRouter.api_route('/read-form/{form_id}', response_description="Read a form from database", methods=["GET"])
async def readForm(form_id: int) -> JSONResponse:
    form = await formController.getOne(form_id)

    response = jsonable_encoder(
        {
            "form": form,
            "detail": "Form read successfully."
        }
    )
    return JSONResponse(content=response, status_code=200)