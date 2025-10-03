from datetime import datetime

from pydantic import BaseModel

from ..enums.task_claim_enum import TaskClaimStatus


# TODO
class CreateTaskClaimSchema(BaseModel):
    task_id: int  # ?

    notes: str | None


# TODO
class UpdateTaskClaimSchema(BaseModel):
    task_id: int  # ?

    start_at: datetime | None
    complete_at: datetime | None
    notes: str | None
    status: TaskClaimStatus
