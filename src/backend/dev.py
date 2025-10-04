import warnings

from hypothesis import find
from hypothesis import strategies as st
from hypothesis.errors import NonInteractiveExampleWarning
from pydantic import BaseModel
from pydantic import Field
from pydantic import NonNegativeInt
from pydantic import PositiveFloat


warnings.filterwarnings('ignore', category=NonInteractiveExampleWarning)


class Model(BaseModel):
    amount: NonNegativeInt = Field(le=400)
    price: PositiveFloat = Field(le=40)


example_1 = find(st.builds(Model), lambda x: True)
print(f'{example_1=}')


example_2 = st.from_type(Model).example()
print(f'{example_2=}')


example_3 = st.builds(Model).example()
print(f'{example_3=}')
