from datetime import date
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

from lib.postgresql.mixin import PostgreSQLMixin, get_connection
from lib.postgresql.utils import postgresql
from modules.user.schemas.response import UserResponseSchema
from tables import user


@postgresql(table=user)
class UserSourceSchema(PostgreSQLMixin, BaseModel):
    id: Optional[UUID] = None

    firstname: str
    lastname: str
    password: str
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


    @classmethod
    async def get_by_email(cls, email: str):
        query = cls.table.select().where(cls.table.c.email==email)
        entity = await get_connection().fetch_one(query=query)
        return cls.from_orm(entity)
        

    async def delete(self):
        query = self.table.delete().where(self.table.c.id==self.id)
        await get_connection().execute(query=query)
        return True