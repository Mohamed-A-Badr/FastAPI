from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"


class User(BaseModel):
    # / Optional means it isn't necessary to to fill it
    # ? we use UUID as the datatype for ID as
    # ? UUID is an encrypted key this provide
    # ? unique key for all the records
    id: Optional[UUID] = uuid4()  # uuid 4 generate random UUID
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]
