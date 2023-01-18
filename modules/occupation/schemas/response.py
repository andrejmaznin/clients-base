from pydantic import BaseModel

class OccResponseSchema(BaseModel):
    id: int
    occupation: str


class ListOccResponseSchema(BaseModel):
    __root__: list[OccResponseSchema]

    class Config:
        orm_mode = True

