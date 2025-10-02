from pydantic import BaseModel


class ItemSchema(BaseModel):
    name: str | None = None
    description: str | None = None
    category: str | None = None
    price: float | None = None
