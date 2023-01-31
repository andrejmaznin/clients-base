from ..clients.source import ClientSourceSchema
from pydantic import BaseModel


class HintClientResponseSchema(BaseModel):
    clients: list[ClientSourceSchema]

    class Config:
        orm_mode = True