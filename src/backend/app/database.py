import typing as t

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel

from . import models  # noqa: F401
from .settings.setting import settings


_async_engine = create_async_engine(settings.async_database_url, echo=True)
_async_session = async_sessionmaker(_async_engine)


async def get_async_session() -> t.AsyncGenerator[AsyncSession, None]:
    async with _async_session() as db:
        yield db


async def init_db() -> None:
    async with _async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
