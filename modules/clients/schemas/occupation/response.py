from pydantic import BaseModel
from uuid import UUID

class OccResponseSchema(BaseModel):
    id: UUID
    occupation: str


class HintResponseSchema(OccResponseSchema):
    dist: float | None
