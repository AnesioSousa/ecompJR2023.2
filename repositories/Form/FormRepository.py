from tortoise.contrib.pydantic import pydantic_model_creator
from models.form.FormModel import Form
from dtos.form.formDTO import FormDTO
from tortoise import Tortoise


class FormRepository:
    def __init__(self):
        self.__entity = Form
        self.__model_creator = pydantic_model_creator(Form)
        #self.__tortoise = Tortoise.get_connection('default')
        
    async def create(self, form: dict) -> FormDTO:
        newForm = await self.__entity.create(**form) 
        return FormDTO.model_validate(await self.toDict(newForm))
    
    async def toDict(self, form: Form) -> dict:
        result = await self.__model_creator.from_tortoise_orm(form)
        return result.model_dump()