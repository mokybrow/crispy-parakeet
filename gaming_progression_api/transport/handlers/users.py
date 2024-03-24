from typing import Annotated

from fastapi import APIRouter
from pydantic import UUID4

from gaming_progression_api.dependencies import UOWDep

from gaming_progression_api.services.users import UsersService
from gaming_progression_api.settings import get_settings

settings = get_settings()


router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.get('/search', description='Поиск пользователей')
async def search_user_by_string(uow: UOWDep, string: str):
    user = await UsersService().search_user(uow, string)
    return user


@router.get('/test', description='Добавление тестовыъ польователей')
async def add_test_users(uow: UOWDep):
    user = await UsersService().add_users(uow)
    return user

