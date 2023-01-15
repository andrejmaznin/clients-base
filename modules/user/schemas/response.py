from datetime import date
from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class UserResponseSchema(BaseModel):
    id: str | UUID

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