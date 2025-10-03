from datetime import datetime

from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import DeclarativeBase
from sqlmodel import Column
from sqlmodel import DateTime
from sqlmodel import Field
from sqlmodel import SQLModel
from sqlmodel import func


class Base(DeclarativeBase):
    metadata = SQLModel.metadata


class User(SQLAlchemyBaseUserTableUUID, Base):
    # phone = Column(String(20))
    # name = Column(String(100), nullable=False)

    # 建立時間（插入時自動設定）
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    # 更新時間（更新時自動更新）
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    )
