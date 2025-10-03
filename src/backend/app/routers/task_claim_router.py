from fastapi import APIRouter
from fastcrud import FilterConfig
from fastcrud import crud_router

from ..dependencies.database_dependency import SessionDepends
from ..dependencies.database_dependency import get_async_session
from ..dependencies.user_dependency import CurrentActiveUserDepends
from ..dependencies.user_dependency import current_active_user
from ..models.task_claim_model import TaskClaim
from ..schemas.task_claim_schema import CreateTaskClaimSchema
from ..schemas.task_claim_schema import UpdateTaskClaimSchema


task_claim_router = APIRouter()


@task_claim_router.post(
    '/task_claim',
    tags=['TaskClaim'],
)
async def create_task_claim(
    data: CreateTaskClaimSchema, user: CurrentActiveUserDepends, session: SessionDepends
) -> TaskClaim:
    model = TaskClaim(**data.model_dump(), creator_id=user.id)
    session.add(model)
    await session.commit()
    await session.refresh(model)
    return model


task_claim_router.include_router(
    crud_router(
        session=get_async_session,
        model=TaskClaim,
        create_schema=CreateTaskClaimSchema,
        update_schema=UpdateTaskClaimSchema,
        path='/task_claim',
        tags=['TaskClaim'],
        create_deps=[],
        read_deps=[],
        read_multi_deps=[],
        update_deps=[current_active_user],
        delete_deps=[current_active_user],
        db_delete_deps=[current_active_user],
        included_methods=[
            # 'create',
            'read',
            'read_multi',
            'update',
            'delete',
            'db_delete',
        ],
        filter_config=FilterConfig(
            is_deleted=lambda: False,
        ),
        select_schema=TaskClaim,
    )
)
