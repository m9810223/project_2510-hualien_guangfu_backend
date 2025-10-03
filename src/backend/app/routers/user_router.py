from contextlib import asynccontextmanager
import typing as t

from fastapi import APIRouter
from fastapi import Depends
from fastapi import FastAPI

from ..database import create_db_and_tables
from ..models.user_model import User
from ..schemas.user_schema import UserCreate
from ..schemas.user_schema import UserRead
from ..schemas.user_schema import UserUpdate
from ..users import auth_backend
from ..users import current_active_user
from ..users import fastapi_users


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Not needed if you setup a migration system like Alembic
    # await create_db_and_tables()
    yield


user_router = APIRouter(lifespan=lifespan)

user_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)
user_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)
user_router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix='/auth',
    tags=['auth'],
)
user_router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix='/auth',
    tags=['auth'],
)
user_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['users'],
)


@user_router.get('/authenticated-route', tags=['auth'])
async def authenticated_route(user: t.Annotated[User, Depends(current_active_user)]):
    return {'message': f'Hello {user.email}!'}
