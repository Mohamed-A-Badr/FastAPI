from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import Gender, Role, User, Update

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Mohamed",
        last_name="Badr",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        # id=uuid4(),
        sid=UUID("41c95313-cda5-4ee3-b09d-88e74aa23173"),
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

'''
    we create a POST method to take the data 
    from the user and send it to the database to 
    append it and store it 

    we send an entity called user which will represent the 
    data coming from the client in the from of User models we 
    create and taken from the user's requset body

    #? we use the same path because one is for GET 
    #? and the other for the POST so there is no conflict 
'''


@app.post("/api/v1/users")
async def adding_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} dosen't exist"
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, update: Update):
    for user in db:
        if user.id == user_id:
            if update.first_name is not None:
                user.first_name = update.first_name
            if update.last_name is not None:
                user.last_name = update.last_name
            if update.middle_name is not None:
                user.middle_name = update.middle_name
            if update.roles is not None:
                user.roles = update.roles
            return

    raise HTTPException(
        staus_code=404,
        detail=f"user with id: {user_id} dosen't exist"
    )
