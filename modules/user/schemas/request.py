from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr


class CreateUserRequestSchema(BaseModel):
    firstname: str
    lastname: str
    password: str
    phone_number: Optional[str] = None
    email: EmailStr
    birthdate: date
    country: Optional[str] = None
    city: Optional[str] = None
    avatar_url: Optional[str] = None

class UpdateUserRequestSchema(BaseModel):
    firstname: str | None
    lastname: str | None
    password: str | None
    phone_number: str | None
    email: EmailStr | None
    birthdate: date | None
    country: str | None
    city: str | None
    avatar_url: str | None
