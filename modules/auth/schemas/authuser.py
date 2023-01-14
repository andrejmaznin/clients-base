from uuid import UUID
from pydantic import BaseModel
from datetime import date

class AuthUser(BaseModel):
    id: UUID
    password: str
    firstname: str
    lastname: str
    phone_number: str | None = None
    email: str
    birthdate: date
    country: str | None = None
    city: str | None = None
    avatar_url: str | None = None
    blocked: bool = False
    confirmed: bool = False

    class Config:
        orm_mode = True