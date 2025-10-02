from fastcrud import crud_router

from ..database import get_async_session
from ..models.item_model import Item
from ..schemas.item_schema import ItemSchema


item_router = crud_router(
    session=get_async_session,
    model=Item,
    create_schema=ItemSchema,
    update_schema=ItemSchema,
    path='/items',
    tags=['Items'],
)
