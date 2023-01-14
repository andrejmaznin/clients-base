from datetime import date
from typing import Optional

from pydantic import BaseModel


class CreateUserRequestSchema(BaseModel):
    firstname: str
    lastname: str
    password: str
    phone_number: Optional[str] = None
    email: str
    birthdate: date
    country: Optional[str] = None
    city: Optional[str] = None
    avatar_url: Optional[str] = None