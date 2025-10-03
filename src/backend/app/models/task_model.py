from datetime import datetime
import typing as t

from sqlmodel import Column
from sqlmodel import DateTime
from sqlmodel import Field
from sqlmodel import SQLModel
from sqlmodel import func

from ..enums.task_enum import TaskDangerLevel
from ..enums.task_enum import TaskStatus
from ..enums.task_enum import TaskType
from ..enums.task_enum import TaskUrgency
from .user_model import UserId


# TODO: index, varchar length, ...
class Task(SQLModel, table=True):
    __tablename__: t.ClassVar[str] = 'task'  # pyright: ignore[reportIncompatibleVariableOverride]

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), nullable=False, server_default=func.now()))
    is_deleted: bool = Field(default=False)
    deleted_at: datetime | None = Field(sa_column=Column(DateTime(timezone=True)))
    updated_at: datetime | None = Field(sa_column=Column(DateTime(timezone=True)))

    id: int = Field(primary_key=True)

    creator_id: UserId = Field(foreign_key='user.id', index=True)

    type: TaskType | None = Field(title='任務類型')
    title: str = Field(title='標題')
    description: str | None = Field(title='簡單敘述')
    status: TaskStatus | None = Field(title='任務狀態')
    start_at: datetime | None = Field(title='開始時間', sa_column=Column(DateTime(timezone=True)))
    deadline: datetime | None = Field(title='截止時間', sa_column=Column(DateTime(timezone=True)))
    contact_number: str | None = Field(title='聯絡電話')
    registration_location: str | None = Field(title='報到地點')
    work_location: str | None = Field(title='工作地點')
    required_number_of_people: int | None = Field(title='需求人數')
    maximum_number_of_people: int | None = Field(title='最大人數')
    urgency: TaskUrgency | None = Field(title='緊急程度')
    danger_level: TaskDangerLevel | None = Field(title='危險程度')
