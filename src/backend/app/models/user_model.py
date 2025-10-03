from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase
from sqlmodel import SQLModel


class Base(DeclarativeBase):
    metadata = SQLModel.metadata


class User(SQLAlchemyBaseUserTableUUID, Base):
    name = Column(String, nullable=True)
    phone = Column(String, nullable=True)

    # 建立時間（插入時自動設定）
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # 更新時間（更新時自動更新）
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
