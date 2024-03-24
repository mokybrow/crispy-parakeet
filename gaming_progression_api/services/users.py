from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import UUID4
from sqlalchemy import func, or_

from gaming_progression_api.models.schemas import Users
from gaming_progression_api.services.unitofwork import IUnitOfWork
from gaming_progression_api.settings import get_settings



class UsersService:
    async def search_user(self, uow: IUnitOfWork, string: str):
        # search = or_(Users.name.contains(string), Users.full_name.contains(string))
        data = string.split()    
        filters = []
        for i in data:
            result = (or_(Users.name.contains(func.lower(i)), Users.surname.contains(i), Users.patronymic.contains(i), Users.email.contains(i)))
            filters.append(or_(result))
        async with uow:
            games = await uow.users.find_user(filters)
            if not games:
                return False
            return games
       
    
    async def add_users(self, uow: IUnitOfWork,):
        # search = or_(Users.name.contains(string), Users.full_name.contains(string))
        users = [
                {"name": "Сергей", "surname": "Сергей", "patronymic": "Сергеевич", "email": "user1@example.com"},
                {"name": "Иван", "surname": "Иванов", "patronymic": "Иванович", "email": "user2@example.com"},
                {"name": "Сидор", "surname": "Сидоров", "patronymic": "Сидорович", "email": "user3@example.com"},

            ]
        async with uow:
            await uow.users.add_many(users)
            await uow.commit()