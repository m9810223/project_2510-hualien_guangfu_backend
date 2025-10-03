from fastapi import APIRouter
from fastcrud import crud_router

from ..database import get_async_session
from ..models.task_model import TaskStatus
from ..models.task_model import TaskType
from ..schemas.task_schema import TaskStatusSchema
from ..schemas.task_schema import TaskTypeSchema


task_router = APIRouter()


task_router.include_router(
    crud_router(
        session=get_async_session,
        model=TaskType,
        create_schema=TaskTypeSchema,
        update_schema=TaskTypeSchema,
        path='/task_type',
        tags=['TaskType'],
        included_methods=[
            'create',
            'read',
            'read_multi',
            # 'update',
            # 'delete',
            # "db_delete",
        ],
        # deleted_methods=[
        #     "create",
        #     "read",
        #     "read_multi",
        #     "update",
        #     "delete",
        #     "db_delete",
        # ],
        # endpoint_names={
        #     # "create": "add",
        #     # "read": "fetch",
        #     # "read_multi": "list",
        #     # "update": "modify",
        #     # "delete": "remove",
        # },
    )
)


task_router.include_router(
    crud_router(
        session=get_async_session,
        model=TaskStatus,
        create_schema=TaskStatusSchema,
        update_schema=TaskStatusSchema,
        path='/task_status',
        tags=['TaskStatus'],
        included_methods=[
            'create',
            'read',
            'read_multi',
            # 'update',
            # 'delete',
            # "db_delete",
        ],
        # deleted_methods=[
        #     "create",
        #     "read",
        #     "read_multi",
        #     "update",
        #     "delete",
        #     "db_delete",
        # ],
        # endpoint_names={
        #     # "create": "add",
        #     # "read": "fetch",
        #     # "read_multi": "list",
        #     # "update": "modify",
        #     # "delete": "remove",
        # },
    )
)
