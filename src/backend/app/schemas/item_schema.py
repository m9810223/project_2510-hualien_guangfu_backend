from datetime import datetime

from pydantic import BaseModel


class CreateItemSchema(BaseModel):
    name: str | None = None
    description: str | None = None
    category: str | None = None
    price: float | None = None


class UpdateItemSchema(BaseModel):
    name: str | None = None
    description: str | None = None
    category: str | None = None
    price: float | None = None


class SelectItemSchema(BaseModel):
    created_at: datetime
    is_deleted: bool = False
    deleted_at: datetime | None
    updated_at: datetime | None

    name: str | None = None
    description: str | None = None
    category: str | None = None
    price: float | None = None
