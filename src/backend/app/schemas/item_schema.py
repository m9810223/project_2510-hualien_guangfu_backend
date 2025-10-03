from pydantic import BaseModel

from ..models.item_model import Item


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


class SelectItemSchema(Item):
    pass
