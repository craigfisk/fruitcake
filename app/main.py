from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Mock user database
fake_users_db = {}

class User(BaseModel):
    email: str
    password: str

class UserInDB(User):
    id: int

class Token(BaseModel):
    access_token: str
    token_type: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_user(db, email: str):
    for user in db.values():
        if user.email == email:
            return user
    return None

@app.post("/users/", response_model=UserInDB)
def create_user(user: User):
    user_id = len(fake_users_db) + 1
    user_in_db = UserInDB(id=user_id, **user.dict())
    fake_users_db[user_id] = user_in_db
    return user_in_db

@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(fake_users_db, form_data.username)
    if not user or user.password != form_data.password:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = "some_token"
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    return {"message": "Successfully logged out"}

@app.get("/")
def read_root():
    return {"Hello": "World"}

