import json
import uuid
from pathlib import Path
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Users API")

DB_FILE = Path("users.txt")


class UserCreate(BaseModel):
    name: str
    email: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None


class User(BaseModel):
    id: str
    name: str
    email: str


def read_users() -> List[User]:
    if not DB_FILE.exists():
        return []
    data = DB_FILE.read_text().strip()
    if not data:
        return []
    return [User(**json.loads(line)) for line in data.splitlines()]


def write_users(users: List[User]) -> None:
    DB_FILE.write_text("\n".join(json.dumps(u.model_dump()) for u in users))


@app.get("/users", response_model=List[User])
def list_users():
    return read_users()


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    users = read_users()
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found.......", headers={"user_id": user_id})


@app.post("/users", response_model=User, status_code=201)
def create_user(payload: UserCreate):
    users = read_users()
    if any(u.email == payload.email for u in users):
        raise HTTPException(status_code=409, detail="Email already registered")
    new_user = User(id=str(uuid.uuid4()), name=payload.name, email=payload.email)
    users.append(new_user)
    write_users(users)
    return new_user


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: str, payload: UserUpdate):
    users = read_users()
    for i, user in enumerate(users):
        if user.id == user_id:
            updated = user.model_copy(update=payload.model_dump(exclude_none=True))
            users[i] = updated
            write_users(users)
            return updated
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: str):
    users = read_users()
    filtered = [u for u in users if u.id != user_id]
    if len(filtered) == len(users):
        raise HTTPException(status_code=404, detail="User not found")
    write_users(filtered)

@app.get("/comments")
def list_comments():
    return "comments"