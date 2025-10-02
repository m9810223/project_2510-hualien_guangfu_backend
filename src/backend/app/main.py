from contextlib import asynccontextmanager

from fastapi import FastAPI

from .routers.item_router import item_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(item_router)
