from pydantic import BaseModel


class TaskTypeSchema(BaseModel):
    name: str


class TaskStatusSchema(BaseModel):
    name: str
