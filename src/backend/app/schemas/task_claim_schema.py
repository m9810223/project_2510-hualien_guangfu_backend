from datetime import datetime

from pydantic import BaseModel
from pydantic import Field

from ..enums.task_claim_enum import TaskClaimStatus


# TODO
class CreateTaskClaimSchema(BaseModel):
    task_id: int  # ?

    notes: str | None = Field(default=None, description='備註')


# TODO
class UpdateTaskClaimSchema(BaseModel):
    task_id: int  # ?

    start_at: datetime | None = Field(default=None, description='開始時間')
    complete_at: datetime | None = Field(default=None, description='完成時間')
    notes: str | None = Field(default=None, description='備註')
    status: TaskClaimStatus = Field(description='認領狀態')
