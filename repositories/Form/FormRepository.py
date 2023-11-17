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
    
    async def getOne(self, id: int) -> FormDTO:
        user = await self.__entity.get_or_none(id=id)
        return FormDTO.model_validate(await self.toDict(user))
    
    async def getAll(self) -> list[FormDTO]:
        users = []
        for user in await self.__entity.all():
            users.append(FormDTO.model_validate(await self.toDict(user)))
        return users