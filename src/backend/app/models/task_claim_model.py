from datetime import datetime
import typing as t

from sqlmodel import CheckConstraint
from sqlmodel import Column
from sqlmodel import DateTime
from sqlmodel import Field
from sqlmodel import SQLModel
from sqlmodel import func

from ..enums.task_claim_enum import TaskClaimStatus
from .user_model import UserId


# TODO: index, varchar length, ...
class TaskClaim(SQLModel, table=True):
    __tablename__: t.ClassVar[str] = 'task_claim'  # pyright: ignore[reportIncompatibleVariableOverride]

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), nullable=False, server_default=func.now()))
    is_deleted: bool = Field(default=False, nullable=False)
    deleted_at: datetime | None = Field(sa_column=Column(DateTime(timezone=True)))
    updated_at: datetime | None = Field(sa_column=Column(DateTime(timezone=True)))

    id: int = Field(primary_key=True)

    creator_id: UserId = Field(foreign_key='user.id')
    task_id: int = Field(foreign_key='task.id')

    start_at: datetime | None = Field(title='開始時間', sa_column=Column(DateTime(timezone=True)))
    complete_at: datetime | None = Field(title='完成時間', sa_column=Column(DateTime(timezone=True)))
    notes: str | None
    status: t.Annotated[str, TaskClaimStatus] = Field(default=TaskClaimStatus.claimed)

    __table_args__ = (
        CheckConstraint(
            f'status IN {tuple(x.value for x in TaskClaimStatus)}',
            name='check_task_claim_status_valid',
        ),
    )
