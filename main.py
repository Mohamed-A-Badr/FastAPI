from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        # ? This line makes our id change every time
        id=uuid4(),  # ? we restart our application
        first_name="Mohamed",
        last_name="Badr",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="habiba",
        last_name="Mohamed",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    ),
]


@app.get("/")
def root():
    return {"Hello": "Mohamed"}
