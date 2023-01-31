
from pydantic import BaseModel, EmailStr, Json
from pydantic.error_wrappers import ErrorWrapper
from lib.postgresql.mixin import PostgreSQLMixin, get_connection
from lib.postgresql.utils import postgresql
from tables import client
from uuid import UUID
from datetime import date


@postgresql(table=client)
class ClientSourceSchema(PostgreSQLMixin, BaseModel):
    id: UUID | None
    user: UUID
    occupation: str
    firstname: str
    lastname: str
    birthdate: date
    city: str
    work_place: str
    income: int
    imgs: dict | Json
    phone_number: str
    email: EmailStr
    linkedin: str | None
    vk: str | None
    instagram: str | None
    telegram_id: str | None


    @classmethod
    async def get_by_user(cls, client_id: UUID, user_id: UUID):
        query = cls.table.select().where(cls.table.c.id==client_id, cls.table.c.user==user_id)
        entity = await get_connection().fetch_one(query=query)
        if entity:
            return cls(**entity)

    async def valid_tg(self):
        if self.telegram_id:
            query = self.table.select().where(
                self.table.c.user == self.user,
                self.table.c.telegram_id == self.telegram_id
            )
            entity = await get_connection().fetch_one(query=query)
            if entity is not None:
                return ValueError(f'Telegram id {self.telegram_id} already exists')
        return True

    async def valid_vk(self):
        if self.vk:
            query = self.table.select().where(
                self.table.c.user == self.user,
                self.table.c.vk == self.vk
            )
            entity = await get_connection().fetch_one(query=query)
            if entity is not None:
                return ValueError(f'Vk {self.vk} already exists')
        return True

    async def valid_instagram(self):
        if self.instagram:
            query = self.table.select().where(
                self.table.c.user == self.user,
                self.table.c.instagram == self.instagram
            )
            entity = await get_connection().fetch_one(query=query)
            if entity is not None:
                return ValueError(f'Instagram {self.instagram} already exists')
        return True

    async def valid_linkedin(self):
        if self.linkedin:
            query = self.table.select().where(
                self.table.c.user == self.user,
                self.table.c.linkedin == self.linkedin
            )
            entity = await get_connection().fetch_one(query=query)
            if entity is not None:
                return ValueError(f'Linkedin {self.linkedin} already exists')
        return True

    async def valid(self):
        errors: list[ErrorWrapper] = []

        insta = await self.valid_instagram()
        vk = await self.valid_vk()
        tg = await self.valid_tg()
        linkin = await self.valid_linkedin()

        if insta is not True:
            errors.append(ErrorWrapper(
                exc=insta,
                loc=(
                    self.firstname,
                    self.lastname,
                    'instagram'
                )
            ))
        if vk is not True:
            errors.append(ErrorWrapper(
                exc=vk,
                loc=(
                    self.firstname,
                    self.lastname,
                    'vk'
                )
            ))
        if tg is not True:
            errors.append(ErrorWrapper(
                exc=tg,
                loc=(
                    self.firstname,
                    self.lastname,
                    'telegram_id'
                )
            ))
        if linkin is not True:
            errors.append(ErrorWrapper(
                exc=linkin,
                loc=(
                    self.firstname,
                    self.lastname,
                    'linkedin'
                )
            ))

        return errors
