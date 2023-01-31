
from pydantic import BaseModel, EmailStr, Json
from lib.postgresql.mixin import PostgreSQLMixin, get_connection
from lib.postgresql.utils import postgresql
from .response import HintClientResponseSchema 
from tables import client
from sqlalchemy import func
from datetime import date
from uuid import UUID


@postgresql(table=client)
class HintClientSourceSchema(PostgreSQLMixin, BaseModel):
    occupation: str | None = ''
    firstname: str | None = ''
    lastname: str | None = ''
    birthdate: date | None
    city: str | None = ''
    work_place: str | None = ''
    income: int | None = 0
    imgs: dict | Json | None
    phone_number: str | None = ''
    email: EmailStr | None = ''
    linkedin: str | None = ''
    vk: str | None = ''
    instagram: str | None = ''
    telegram_id: str | None = ''


    async def get_hint(self, user_id: UUID, ratio: float = 0.4, income_sign: str = '>', date_sign: str = '<') -> HintClientResponseSchema:
        element_count = len(self.dict(exclude_defaults=True))

        if self.birthdate is None:
            self.birthdate = func.now()
        
        signs = {
            '<': (self.table.c.income <= self.income, self.table.c.birthdate <= self.birthdate),
            '>': (self.table.c.income >= self.income, self.table.c.birthdate >= self.birthdate)
        }

        query = self.table.select().where((
            func.similarity(self.table.c.occupation, self.occupation) +
            func.similarity(self.table.c.firstname, self.firstname) +
            func.similarity(self.table.c.lastname, self.lastname) +
            func.similarity(self.table.c.city, self.city) +
            func.similarity(self.table.c.work_place, self.work_place) +
            func.similarity(self.table.c.phone_number, self.phone_number) +
            func.similarity(self.table.c.email, self.email) +
            func.similarity(self.table.c.linkedin, self.linkedin) +
            func.similarity(self.table.c.vk, self.vk) +
            func.similarity(self.table.c.instagram, self.instagram) +
            func.similarity(self.table.c.telegram_id, self.telegram_id)
        ) / element_count > ratio, signs[income_sign][0], signs[date_sign][1], self.table.c.user == user_id)
        entity = await get_connection().fetch_all(query=query)
        return HintClientResponseSchema(clients=entity)