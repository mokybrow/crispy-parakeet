from functools import lru_cache

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from gaming_progression_api.settings import get_settings

from gaming_progression_api.transport.handlers.users import router as users_router



def _setup_api_routers(
    api: APIRouter,
) -> None:

    api.include_router(users_router)



@lru_cache
def make_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
     
    )
    origins = [
        'http://localhost:3000',
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    _setup_api_routers(app.router)
    return app
