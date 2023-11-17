from repositories.Form.FormRepository import FormRepository
from dtos.form.formDTO import FormDTO
from fastapi import HTTPException

class FormController():
    def __init__(self) -> None:
        self.__repository = FormRepository()

    async def create(self, form: dict[str, any]) -> FormDTO:
        try:
            new_form = await self.__repository.create(form)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error was ocurred: {str(e)}")
        return new_form