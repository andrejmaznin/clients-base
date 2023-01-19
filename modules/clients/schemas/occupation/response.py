from pydantic import BaseModel
from typing import List

class OccResponseSchema(BaseModel):
    id: int
    occupation: str
    dist: float | None

class ListOccResponseSchema(BaseModel):
    __root__: List[OccResponseSchema]

    class Config:
        orm_mode = True
