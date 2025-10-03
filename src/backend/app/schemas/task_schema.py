from datetime import datetime

from pydantic import BaseModel

from ..enums.task_enum import TaskDangerLevel
from ..enums.task_enum import TaskStatus
from ..enums.task_enum import TaskType
from ..enums.task_enum import TaskUrgency
from ..models.task_model import Task


class CreateTaskSchema(BaseModel):
    title: str


class UpdateTaskSchema(BaseModel):
    type: TaskType | None
    title: str
    description: str | None
    status: TaskStatus | None
    start_at: datetime | None
    deadline: datetime | None
    contact_number: str | None
    registration_location: str | None
    work_location: str | None
    required_number_of_people: int | None
    maximum_number_of_people: int | None
    urgency: TaskUrgency | None
    danger_level: TaskDangerLevel | None


class SelectTaskSchema(Task):
    pass
