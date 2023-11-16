from tortoise.contrib.pydantic import pydantic_model_creator
from dtos.user.userDTO import UserDTO
from models.user.UserModel import User
from tortoise import Tortoise

class UserRepository:
    def __init__(self):
        self.__entity = User
        self.__model_creator = pydantic_model_creator(User)
        self.__tortoise = Tortoise.get_connection('default')

    async def toDict(self, user: User) -> dict:
        result = await self.__model_creator.from_tortoise_orm(user)
        return result.model_dump()

    async def create(self, user: dict) -> UserDTO:
        newUser = await self.__entity.create(**user) 
        return UserDTO.model_validate(await self.toDict(newUser))
    
    async def update(self, userDTO: UserDTO) -> UserDTO:
        user = User(**userDTO.model_dump())
        await user.save(force_update=True)
        return UserDTO.model_validate(await self.toDict(user))

    async def getOne(self, id: int) -> UserDTO:
        user = await self.__entity.get_or_none(id=id)
        return UserDTO.model_validate(await self.toDict(user))
    
    async def getAll(self) -> list[UserDTO]:
        users = []
        for user in await self.__entity.all():
            users.append(UserDTO.model_validate(await self.toDict(user)))
        return users
    
    async def getMany(self, key: str, value: any) -> list[UserDTO]:
        users = list[UserDTO]
        for user in await self.__entity.filter(**{key:value}):
            users.append(UserDTO.model_validate(await self.toDict(user)))
        return users

    async def delete(self, id: int) -> bool:
        user = await self.__entity.get_or_none(id=id)
        if user:
            await user.delete()
            return True
        return False
    
    # async def execute_sql(self, query: str) -> list[dict]:
    #     return await self.__tortoise.execute_query_dict(query)