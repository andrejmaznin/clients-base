from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from lib.postgresql.mixin import PostgreSQLMixin
from lib.postgresql.utils import postgresql
from modules.user.schemas.response import UserResponseSchema
from tables import user


@postgresql(table=user)
class UserSourceSchema(PostgreSQLMixin, BaseModel):
    id: Optional[UUID] = None

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

    def get_response(self):
        return UserResponseSchema(
            id=str(self.id),
            firstname=self.firstname,
            lastname=self.lastname,
            phone_number=self.phone_number,
            email=self.email,
            birthdate=self.birthdate,
            country=self.country,
            city=self.city,
            avatar_url=self.avatar_url,
            blocked=self.blocked,
            confirmed=self.confirmed
        )
