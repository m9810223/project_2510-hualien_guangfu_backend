from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware

from .routers.item_router import item_router
from .routers.user_router import user_router
from .settings.app_setting import app_settings


def _custom_generate_unique_id(route: APIRoute) -> str:
    return f'{route.tags[0]}-{route.name}'


@asynccontextmanager
async def _lifespan(app: FastAPI):
    yield


app = FastAPI(
    lifespan=_lifespan,
    title=app_settings.PROJECT_NAME,
    openapi_url=f'{app_settings.API_V1_STR}/openapi.json',
    generate_unique_id_function=_custom_generate_unique_id,
)


# Set all CORS enabled origins
if app_settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=app_settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )


app.include_router(user_router)

app.include_router(item_router)  # TODO
