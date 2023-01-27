from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import date


class ClientRequestSchema(BaseModel):
    occupation: str
    firstname: str
    lastname: str
    birthdate: date
    city: str
    work_place: str
    income: int
    imgs: dict
    phone_number: str
    email: EmailStr
    linkedin: str | None
    vk: str | None
    instagram: str | None
    telegram_id: str | None

class UpdateClientRequestSchema(BaseModel):
    occupation: str | None
    firstname: str | None
    lastname: str | None
    birthdate: date | None
    city: str | None
    work_place: str | None
    income: int | None
    imgs: dict | None
    phone_number: str | None
    email: EmailStr | None
    linkedin: str | None
    vk: str | None
    instagram: str | None
    telegram_id: str | None


class DeleteClientRequestSchema(BaseModel):
    id: list[UUID]