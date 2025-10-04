from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .logger import get_logger
from .routers.item_router import item_router
from .routers.task_claim_router import task_claim_router
from .routers.task_router import task_router
from .routers.user_router import user_router
from .settings.app_setting import app_settings


logger = get_logger()


@asynccontextmanager
async def _lifespan(app: FastAPI):
    yield


app = FastAPI(
    lifespan=_lifespan,
    title=app_settings.PROJECT_NAME,
    openapi_url=f'{app_settings.API_V1_STR}/openapi.json',
)


logger.info(f'allow_origins: {app_settings.all_cors_origins}')
if app_settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=app_settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )


app.include_router(task_claim_router, prefix=app_settings.API_V1_STR)
app.include_router(task_router, prefix=app_settings.API_V1_STR)
app.include_router(item_router, prefix=app_settings.API_V1_STR)  # TODO
app.include_router(user_router, prefix=app_settings.API_V1_STR)


app.include_router(task_claim_router)
app.include_router(task_router)
app.include_router(user_router)
