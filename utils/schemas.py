import math
import pydantic
from datetime import datetime
from typing import Union, List

class User(pydantic.BaseModel):
  firstName: str
  lastName: str
  email: str
  _id: int | None = None
  nickname: Union[List[str], None] = None
  createdAt: datetime = math.trunc(datetime.now().timestamp() * 1000)