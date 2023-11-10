from fastapi import Response, Request, HTTPException
from models.user.UserModel import User
from repositories.User.UserRepository import UserRepository


class UserController():

    def __init__(self) -> None:
        self.__repository = UserRepository()

    async def create(self, user: dict) -> User:
        try:
            new_user = await self.__repository.create(user)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error was ocurred: {str(e)}")
        return new_user

    async def getOne(self, id: int) -> User:
        user = await self.__repository.get_one(id=id)
        return user    
    async def getAll(self) -> list[User]:
        users = await self.getAll()
        return users
    
    async def update(self, user: dict) -> User:
        searched_user = None
        try:
            searched_user = await self.__repository.get_one(id=user['id'])
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error was ocurred: {str(e)}")
        
        try:
            if searched_user:
                searched_user.name = user['name']
                searched_user.email = user['email']
                searched_user.password = user['password']
                searched_user = await self.__repository.update(searched_user)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error was ocurred: {str(e)}")
        return searched_user

        

    async def delete(self, id: int) -> bool:
        searched_user = None
        try:
            searched_user = await self.__repository.get_one(id=id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error was ocurred: {str(e)}")
        
        try:
            if searched_user:
                return await self.__repository.delete(searched_user)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error was ocurred: {str(e)}")
        return False