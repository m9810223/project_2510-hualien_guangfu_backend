import typing as t

from sqlmodel import Field
from sqlmodel import SQLModel


class Item(SQLModel, table=True):
    __tablename__: t.ClassVar[str] = 'items'  # pyright: ignore[reportIncompatibleVariableOverride]
    id: int = Field(primary_key=True, nullable=False)

    name: str
    description: str
    category: str
    price: int
