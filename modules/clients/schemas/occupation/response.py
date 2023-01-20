from pydantic import BaseModel


class OccResponseSchema(BaseModel):
    id: int
    occupation: str


class HintResponseSchema(OccResponseSchema):
    dist: float | None
