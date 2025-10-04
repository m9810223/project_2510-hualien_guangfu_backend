from datetime import datetime

from pydantic import BaseModel
from pydantic import Field

from ..enums.task_enum import TaskDangerLevel
from ..enums.task_enum import TaskStatus
from ..enums.task_enum import TaskType
from ..enums.task_enum import TaskUrgency


class CreateTaskSchema(BaseModel):
    type: TaskType | None = Field(default=None, description='任務類型')
    title: str = Field(default=..., description='標題')
    description: str | None = Field(default=None, description='簡單敘述')
    status: TaskStatus | None = Field(default=None, description='任務狀態')
    start_at: datetime | None = Field(default=None, description='開始時間')
    deadline: datetime | None = Field(default=None, description='截止時間')
    contact_number: str | None = Field(default=None, description='聯絡電話')
    registration_location: str | None = Field(default=None, description='報到地點')
    work_location: str | None = Field(default=None, description='工作地點')
    required_number_of_people: int | None = Field(default=None, description='需求人數')
    maximum_number_of_people: int | None = Field(default=None, description='最大人數')
    urgency: TaskUrgency | None = Field(default=None, description='緊急程度')
    danger_level: TaskDangerLevel | None = Field(default=None, description='危險程度')


class UpdateTaskSchema(BaseModel):
    type: TaskType | None = Field(default=None, description='任務類型')
    title: str = Field(description='標題')
    description: str | None = Field(default=None, description='簡單敘述')
    status: TaskStatus | None = Field(default=None, description='任務狀態')
    start_at: datetime | None = Field(default=None, description='開始時間')
    deadline: datetime | None = Field(default=None, description='截止時間')
    contact_number: str | None = Field(default=None, description='聯絡電話')
    registration_location: str | None = Field(default=None, description='報到地點')
    work_location: str | None = Field(default=None, description='工作地點')
    required_number_of_people: int | None = Field(default=None, description='需求人數')
    maximum_number_of_people: int | None = Field(default=None, description='最大人數')
    urgency: TaskUrgency | None = Field(default=None, description='緊急程度')
    danger_level: TaskDangerLevel | None = Field(default=None, description='危險程度')
