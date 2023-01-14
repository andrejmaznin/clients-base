from jose import JWTError, jwt
from os import getenv
from tables import user
from lib.postgresql import get_connection
from datetime import date
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


ALGORITHM = "HS256"
SECRET_KEY = getenv("SECRET_KEY")

class User(BaseModel):
    id: UUID

    firstname: str
    lastname: str
    phone_number: Optional[str] = None
    email: str
    birthdate: date
    country: Optional[str] = None
    city: Optional[str] = None
    avatar_url: Optional[str] = None
    blocked: bool = False
    confirmed: bool = False

    class Config:
        orm_mode = True



def create_access_token(data: dict) -> str | None:
    data["id"] = str(data["id"])
    del data["birthdate"]
    if SECRET_KEY:
        encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    return None


async def get_current_user(token: str) -> None | User:
    if SECRET_KEY:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        query = user.select().where(
            user.c.id == payload.get("id"), 
            user.c.email == payload.get("email"),
            user.c.phone_number == payload.get("phone_number"),
        )
        
        entity = await get_connection().fetch_one(query)
        if entity:
            return User.from_orm(entity)
        return None
    return None

