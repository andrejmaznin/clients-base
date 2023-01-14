from datetime import date
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


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