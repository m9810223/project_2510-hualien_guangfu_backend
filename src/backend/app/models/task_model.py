import typing as t

from sqlalchemy import Text
from sqlmodel import Column
from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel


class TaskType(SQLModel, table=True):
    __tablename__: t.ClassVar[str] = 'task_types'  # pyright: ignore[reportIncompatibleVariableOverride]

    type: str = Field(max_length=50, primary_key=True)
    display_name: str = Field(max_length=100)
    description: str | None = Field(default=None, sa_column=Column(Text))
    icon: str | None = Field(default=None, max_length=100)

    # 關聯
    tasks: list['Task'] = Relationship(back_populates='task_type_obj')


class TaskStatus(SQLModel, table=True):
    __tablename__: t.ClassVar[str] = 'task_statuses'  # pyright: ignore[reportIncompatibleVariableOverride]

    status: str = Field(max_length=50, primary_key=True)
    display_name: str = Field(max_length=100)
    description: str | None = Field(default=None, sa_column=Column(Text))

    # 關聯
    tasks: list['Task'] = Relationship(back_populates='task_status_obj')


# class Task(SQLModel, table=True):
#     __tablename__: t.ClassVar[str] = 'tasks'  # pyright: ignore[reportIncompatibleVariableOverride]

#     id: int = Field(primary_key=True)

#     creator_id: int = Field(foreign_key='users.id', index=True)
#     title: str = Field(max_length=200)
#     description: str = Field(sa_column=Column(Text))
#     task_type: str = Field(foreign_key='task_types.type', max_length=50)
#     status: str = Field(default='available', foreign_key='task_statuses.status', max_length=50, index=True)
#     location_data: dict = Field(sa_column=Column(JSON))  # {address, coordinates, details}
#     required_volunteers: int = Field(default=1)
#     required_skills: dict | None = Field(default=None, sa_column=Column(JSON))  # 所需技能或資格
#     deadline: datetime | None = Field(default=None)
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
