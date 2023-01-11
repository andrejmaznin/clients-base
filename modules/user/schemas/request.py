from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateUserRequestSchema(BaseModel):
    firstname: str
    lastname: str
    phone_number: Optional[str] = None
    email: str
    birthdate: datetime
    country: Optional[str] = None
    city: Optional[str] = None
    avatar_url: Optional[str] = None
