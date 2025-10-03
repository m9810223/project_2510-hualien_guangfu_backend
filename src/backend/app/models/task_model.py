from datetime import datetime
import typing as t

from fastapi_users_db_sqlalchemy import UUID_ID
from sqlmodel import Column
from sqlmodel import DateTime
from sqlmodel import Field
from sqlmodel import SQLModel
from sqlmodel import func


class TaskType(SQLModel, table=True):
    __tablename__: t.ClassVar[str] = 'task_type'  # pyright: ignore[reportIncompatibleVariableOverride]

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    is_deleted: bool = False
    deleted_at: datetime | None = Field(sa_column=Column(DateTime(timezone=True)))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True)))

    id: int = Field(primary_key=True)

    name: str = Field(unique=True)  # 鏟土 / 搬運


class TaskStatus(SQLModel, table=True):
    __tablename__: t.ClassVar[str] = 'task_status'  # pyright: ignore[reportIncompatibleVariableOverride]

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    is_deleted: bool = False
    deleted_at: datetime | None = Field(sa_column=Column(DateTime(timezone=True)))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True)))

    id: int = Field(primary_key=True)

    name: str = Field(unique=True)


class Task(SQLModel, table=True):
    __tablename__: t.ClassVar[str] = 'task'  # pyright: ignore[reportIncompatibleVariableOverride]

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    is_deleted: bool = False
    deleted_at: datetime | None = Field(sa_column=Column(DateTime(timezone=True)))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True)))

    id: int = Field(primary_key=True)

    task_type_id: int = Field(foreign_key='task_type.id')
    task_status_id: int = Field(foreign_key='task_status.id')
    creator: UUID_ID = Field(foreign_key='user.id', index=True)
    title: str
    description: str

    #     deadline: datetime | None = Field(default=None)

    #     location_data: dict = Field(sa_column=Column(JSON))  # {address, coordinates, details}
    #     required_volunteers: int = Field(default=1)
    #     required_skills: dict | None = Field(default=None, sa_column=Column(JSON))  # 所需技能或資格
    #     priority_level: int = Field(default=1)  # 1-5, 5為最高優先級
    #     approval_status: str = Field(default='approved', max_length=20)  # 'pending', 'approved', 'rejected'
    #     approved_by: int | None = Field(default=None, foreign_key='users.id')
    #     approved_at: datetime | None = Field(default=None)

    #     # 關聯
    #     creator: 'User' = Relationship(
    #         sa_relationship_kwargs={'foreign_keys': '[Task.creator_id]'},
    #     )
    #     approver: 'User | None' = Relationship(
    #         sa_relationship_kwargs={'foreign_keys': '[Task.approved_by]'},
    #     )
    #     task_type_obj: TaskType = Relationship(back_populates='tasks')
    #     task_status_obj: TaskStatus = Relationship(back_populates='tasks')
    #     task_claims: list['TaskClaim'] = Relationship(back_populates='task')
    #     need_assignments: list['NeedAssignment'] = Relationship(back_populates='task')
    #     supply_reservations: list['SupplyReservation'] = Relationship(back_populates='task')


# class TaskClaim(SQLModel, table=True):
#     __tablename__: t.ClassVar[str] = 'task_claims'  # pyright: ignore[reportIncompatibleVariableOverride]

#     id: int = Field(primary_key=True)

#     task_id: int = Field(sa_column=Column(ForeignKey('tasks.id', ondelete='CASCADE'), nullable=False))
#     user_id: int = Field(foreign_key='users.id')
#     claimed_at: datetime = Field(sa_column_kwargs={'server_default': func.now()})
#     started_at: datetime | None = Field(default=None)
#     completed_at: datetime | None = Field(default=None)
#     notes: str | None = Field(default=None, sa_column=Column(Text))
#     status: str = Field(default='claimed', max_length=20)  # 'claimed', 'started', 'completed', 'cancelled'

#     # 關聯
#     task: Task = Relationship(back_populates='task_claims')
#     user: 'User' = Relationship(back_populates='task_claims')
