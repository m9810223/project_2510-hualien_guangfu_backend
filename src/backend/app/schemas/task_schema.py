from datetime import datetime

from pydantic import BaseModel

from ..enums.task_enum import TaskDangerLevel
from ..enums.task_enum import TaskStatus
from ..enums.task_enum import TaskType
from ..enums.task_enum import TaskUrgency


class CreateTaskSchema(BaseModel):
    type: TaskType | None = None
    title: str
    description: str | None = None
    status: TaskStatus | None = None
    start_at: datetime | None = None
    deadline: datetime | None = None
    contact_number: str | None = None
    registration_location: str | None = None
    work_location: str | None = None
    required_number_of_people: int | None = None
    maximum_number_of_people: int | None = None
    urgency: TaskUrgency | None = None
    danger_level: TaskDangerLevel | None = None


class UpdateTaskSchema(BaseModel):
    type: TaskType | None = None
    title: str
    description: str | None = None
    status: TaskStatus | None = None
    start_at: datetime | None = None
    deadline: datetime | None = None
    contact_number: str | None = None
    registration_location: str | None = None
    work_location: str | None = None
    required_number_of_people: int | None = None
    maximum_number_of_people: int | None = None
    urgency: TaskUrgency | None = None
    danger_level: TaskDangerLevel | None = None
