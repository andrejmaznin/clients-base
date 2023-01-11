from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserResponseSchema(BaseModel):
    id: str

    firstname: str
    lastname: str
    phone_number: Optional[str] = None
    email: str
    birthdate: datetime
    country: Optional[str] = None
    city: Optional[str] = None
    avatar_url: Optional[str] = None
    blocked: bool = False
    confirmed: bool = False
