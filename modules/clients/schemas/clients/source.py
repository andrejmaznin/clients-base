
from pydantic import BaseModel, validator
from lib.postgresql.mixin import PostgreSQLMixin
from lib.postgresql.utils import postgresql
from tables import client
from uuid import UUID
from datetime import date
from modules.clients.schemas.occupation.source import OccSourceSchema


@postgresql(table=client)
class ClientSourceSchema(PostgreSQLMixin, BaseModel):
    id: UUID | None
    user: UUID
    occupation: str
    firstname: str
    birthdate: date
    city: str
    work_place: str
    income: int
    imgs: dict
    phone_number: str
    email: str
    linkedin: str
    vk: str
    instagram: str
    telegram_id: str

