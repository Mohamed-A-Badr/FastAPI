from typing import List
from uuid import UUID, uuid4
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
        # id=uuid4(),
        # ? this way make the id fixed
        id=UUID("41c95313-cda5-4ee3-b09d-88e74aa23173"),
        first_name="habiba",
        last_name="Mohamed",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    ),
]


@app.get("/")
def root():
    return {"Hello": "Mohamed"}


@app.get("/api/v1/users")
async def fetch_users():
    return db
