from tortoise.contrib.pydantic import pydantic_model_creator
from models.user.UserModel import User
from tortoise import Tortoise

class UserRepository:
    def __init__(self):
        self.__entity = User
        self.__model_creator = pydantic_model_creator(User)
        self.__tortoise = Tortoise.get_connection('default')

    async def to_dict(self, user: User) -> dict:
        result = await self.__model_creator.from_tortoise_orm(user)
        return result.model_dump()

    async def create(self, user: dict) -> User:
        return await self.__entity.create(**user)
    
    async def update(self, user: User) -> User:
        await user.save()
        return user

    async def get_one(self, id: int) -> User:
        return await self.__entity.get_or_none(id=id)
    
    async def get_all(self) -> list[User]:
        return await self.__entity.all()
    
    async def get_many(self, key: str, value: any) -> list[User]:
        return await self.__entity.filter(**{key:value})

    async def delete(self, user: User) -> bool:
        await user.delete()
        return True
    
    async def execute_sql(self, query: str) -> list[dict]:
        return await self.__tortoise.execute_query_dict(query)