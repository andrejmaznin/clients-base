from pydantic import BaseModel, Json
from datetime import date
import json



class ClientRequestSchema(BaseModel):
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